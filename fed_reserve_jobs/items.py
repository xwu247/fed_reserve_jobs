# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FedReserveJobsItem(scrapy.Item):
    job_id = scrapy.Field()
    job_name = scrapy.Field()
    job_location = scrapy.Field()
    job_posting = scrapy.Field()
