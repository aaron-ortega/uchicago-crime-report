import re
import os
import logging
import pandas as pd
from pandas.api import types
from datetime import datetime
from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut
from tqdm import tqdm
from glob import glob
import path_update

def tag_incident(incident):
	"""
	Tag common incidents using a regex
	"""
	try:
		return re.findall(regex, incident)[0]
	except TypeError:
		return pd.np.nan
	except IndexError:
		return pd.np.nan

	
def approx_date(date):
	"""
	Takes a pandas Series of lists containing datetime string
	information and approximates datetime.

	Returns
	-------
	Datetime type
	"""
	if isinstance(date, float):
		log2.info(f'Failed to parse: {date}')
		return pd.Timestamp(pd.np.nan) 
	
	try:
		if len(date) == 1:
			return pd.to_datetime(date[0], errors='coerce')
	
		elif len(date) == 2:
			time1 = pd.to_datetime(date[0])
			time2 = pd.to_datetime(re.findall(r"\d+/\d+/\d+", date[0])[0] + date[1])
	
			diff = time2 - time1
		
			if diff < pd.Timedelta(6, 'h'):
				return time1 + diff/2
			else:
				return pd.Timestamp(pd.np.nan)
	
		else:
			time1 = pd.to_datetime(date[0])
			time2 = pd.to_datetime(re.findall(r"\d+/\d+/\d+", date[1])[0])
		
			diff = time2 - time1
			
			if diff < pd.Timedelta(6, 'h'):
				return time1 + diff/2
			else:
				return pd.Timestamp(pd.np.nan)
			
	except ValueError as err:
		log2.info(f'{err}::{date}')
		return pd.Timestamp(pd.np.nan)

	except IndexError as err:
		log2.info(f'{err}::{date}')
		return pd.Timestamp(pd.np.nan)
	
	except OutOfBoundsDatetime as err:
		log2.info(f'{err}::{date}')
		return pd.Timestamp(pd.np.nan)

	
def add_avenue(address):

	avenues = 'cottage grove,drexel,ingleside,ellis,greenwood,university,\
	woodlawn,kimbark,kenwood,dorchester,blackstone,harper,\
	lake park,stony island,cornell,everett'.split(',')
	
	for ave in avenues:
		if re.search(ave, address):
			address += ' avenue'
			break

	return address


def address_to_coordinates(address):
	'''
	Function takes an address as a string and formats to improve 
	likelihood of getting gps coordinatesd.

	Returns
	-------
	If location found: a tuple containing the latitude & longitude
	If not: an integer code (user defined)
	'''
	
	address = re.sub(r' \(.*\)', '', address) # remove parenthetical info
	address = re.sub(r' at|and ', ' & ', address) # fix intersection
	
	try:
		# Check if address is between streets
		# E.g. (52nd St. between Greenwood & University)
		pattern = re.findall(r'(\w.*(?= between)) between ((?<=between )\w.*(?= &)) & ((?<=\& )\w.*)', address)[0]
		street_1 = f"{pattern[0]} {pattern[1]}"
		street_2 = f"{pattern[0]} {pattern[2]}"
		
		# Server timeout time is 10sec
		location_1 = geocoder.geocode(add_avenue(street_1), timeout=10)
		location_2 = geocoder.geocode(add_avenue(street_2), timeout=10)
		
		# Returns midpoint between the two locations
		lat = (location_1.latitude + location_2.latitude)/2
		long = (location_1.longitude + location_2.longitude)/2
		return lat, long
	
	except IndexError:
		# Only single address
		location = geocoder.geocode(address, timeout=10)
		if location != None:
			return (location.latitude, location.longitude)
		 
	except GeocoderTimedOut as timeout:
		# Server timeout value if any (check later)
		log1.info(f"{timeout}::{address}")
		return pd.np.nan, pd.np.nan
		 
	except Exception as err:
		log1.info(f"Unexpected error: {err} for {address}")
		return pd.np.nan, pd.np.nan
		 

def set_logger(logger_name, log_file, level=logging.INFO):
	"""
	Configure logging parameters
	"""
	logger = logging.getLogger(logger_name)
	logger.setLevel(level)
	
	file_handler = logging.FileHandler(log_file)
	formatter = logging.Formatter('%(levelname)s::%(name)s::%(message)s')
	file_handler.setFormatter(formatter)
	logger.addHandler(file_handler)

	
if "__main__" == __name__:
	
	# Working directory
	dir_ = '/Users/aaron/Documents/github/uchicago-crime-report'
	os.chdir(dir_)
	
	# Configure logging
	today = datetime.now().date()
	
	logger_name = ['geocoder', 'approx_date']
	log_file = [f'logs/geocoder-{today}.log', f'logs/approx_date-{today}.log']
	set_logger(logger_name[0], log_file[0])
	set_logger(logger_name[1], log_file[1])
	log1 = logging.getLogger('geocoder')
	log2 = logging.getLogger('approx-date')
	
	# Import data
	#path = 'data/raw_crimeLogData.json'
	path = glob('data/*.json')[-1]
	df = pd.read_json(path)
	#df.rename(columns={'Occured':'Occurred'}, inplace=True)
	
	# Drop nan and useless columns
	del df['Disposition']
	del df['UCPD_ID']
	df.dropna(axis=0, how='all', inplace=True)
	
	# Lowercase and remove whitespace
	df = df.applymap(lambda df: str.lower(df).strip() if isinstance(df, str) else df)
	
	# Remove bad Incident data
	remove = 'void|:|no incident reports'
	df = df[~df.Incident.str.contains(f'{remove}')]
	
	# Tag common incidents using a regex
	common_incidents = 'lost|assault|theft|robbery|battery|mental health|burglary'
	regex = re.compile(f'{common_incidents}') # Used in method: tag_incident
	
	# Add Tag column
	df['Tag'] = df['Incident'].apply(tag_incident)
	print('Tags: Done')
	
	# Add approx_occurred column
	date = df.Occurred.str.split(pat=r'to')
	df['approx_occurred'] = date.apply(approx_date)
	assert types.is_datetime64_any_dtype(df.approx_occurred)
	print('Dates approximated: Done')
	
	# Setup geocoder
	with open('google-maps-api/api-key.txt', 'r') as f:
		key = f.readline()
		geocoder = GoogleV3(api_key=key,
							user_agent="uchicago_surronding_area",
							format_string="%s, Chicago, IL")
	
	# Add latitude and longitude columns
	tqdm.pandas(desc="Geocoding") # Add CL progress bar
	df[['latitude', 'longitude']] = df['Location'].progress_apply(address_to_coordinates).apply(pd.Series)
	assert types.is_float_dtype(df['latitude'])
	assert types.is_float_dtype(df['longitude'])
	print('Geocoding: Done')
	
	# Save cleaned data
	df.reset_index(drop=True, inplace=True)
	df.to_csv(f'data/test_data-{today}.csv', index=False)

	# create tmp file to update scrape url
	one_day = pd.Timedelta(1, 'D')
	time_range = (df.Reported.iloc[[-1]]
				  .str
				  .findall(r'(\d+/\d+/\d+)')
				  .apply(lambda x: pd.to_datetime(x[0]) + one_day)
				 )
	
	# Scrape every week
	time_range = time_range.append(time_range + pd.Timedelta(6, 'D'))
	
	# Save tmp file with time range
	time_range.to_csv('logs/tmp.txt',
					  index=False,
					  header=False,
					  date_format='%m-%d-%Y'
					 )
	
	# Run path_update.py
	path_update.update()
	
	print('#### Done ####')
