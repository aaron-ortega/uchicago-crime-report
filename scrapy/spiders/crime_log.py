import scrapy

class crimeLog(scrapy.Spider):
	name = 'crimeLog'
	AUTOTHROTTLE_ENABLED = True
	host_name = 'https://incidentreports.uchicago.edu/'
	start_urls =['https://incidentreports.uchicago.edu/incidentReportArchive.php?startDate=07%2F01%2F2010&endDate=09%2F19%2F2018',]
	
	def parse(self, response):

		item_names = 'Incident,Location,Reported,Occured,Comments,Disposition,UCPD_ID'.split(',')
		data_table = response.xpath('//table[@class="table ucpd"]/tbody')
		
		# 5 reports per page
		# xpath index starts at 1
		for num in range(1, 6):
			data = data_table.xpath('tr[{}]/td/text()'.format(num)).extract()
			yield (dict(zip(item_names, data)))

		next_page = response.xpath('//ul[@class="pager"]/li[@class="next "]/a/@href').extract()
		try:
			url = crimeLog.host_name + next_page[0]
			yield scrapy.Request(url, callback=self.parse)
		except IndexError:
			print('#####################\nNo next page.\nDone scraping!\n#####################')
