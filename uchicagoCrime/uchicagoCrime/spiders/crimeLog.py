import scrapy

class crimeLog(scrapy.Spider):
    
    # Settings
    name = 'crimeLog'
    AUTOTHROTTLE_ENABLED = True
    host_name = 'https://incidentreports.uchicago.edu/'
    file_path = '/Users/aaron/Documents/github/uchicago-crime-report/logs/scrape_path.log'
    
    # Read time range for scrape
    with open(file_path, 'r') as f:
        url = f.readlines()[-1]
    
    # Start
    start_urls = [f'{url}',]

    def parse(self,response):
        item_names = 'Incident,Location,Reported,Occurred,Comments,Disposition,UCPD_ID'.split(',')
        data_table = response.xpath('//table[@class="table ucpd"]/tbody')
        
        # 5 reports per page
        # xpath index starts at 1
        for num in range(1,6):

            data = data_table.xpath('tr[{}]/td/text()'.format(num)).extract()
            if data == []:
                continue
            
            yield dict(zip(item_names, data))
            
        next_page = response.xpath('//ul[@class="pager"]/li[@class="next "]/a/@href').extract()
        try:
            url = crimeLog.host_name + next_page[0]
            yield scrapy.Request(url, callback=self.parse)
        except IndexError:
            print('#####################\nNo next page.\nDone scraping!\n#####################')
