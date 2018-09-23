# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrimemapItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()

	Incident = scrapy.Field()
	Location = scrapy.Field()
	Reported = scrapy.Field()
	Occurred = scrapy.Field()
	Comments = scrapy.Field()
	Disposition = scrapy.Field()
	UCPD_ID = scrapy.Field()
