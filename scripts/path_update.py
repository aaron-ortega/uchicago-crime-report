import os
import re

def update():
	
	# Directory settings
	path = '/Users/aaron/Documents/github/uchicago-crime-report/logs'
	os.chdir(path)

	# Url format
	url = 'https://incidentreports.uchicago.edu/incidentReportArchive.php?startDate={}%2F{}%2F{}&endDate={}%2F{}%2F{}'

	with open('tmp.txt', 'r') as t:
		read = t.readlines()
		start = re.findall(r'\d+', read[0])
		end = re.findall(r'\d+', read[1])

		# Update url
		url = url.format(*start, *end)

		with open('scrape_path.log', 'a') as f:
			f.write(f'\n{url}')

	os.remove('tmp.txt')
