# -*- coding: utf-8 -*-
import scrapy
from items import CarscraperItem

class CarenginesSpider(scrapy.Spider):
    name = 'carEngines'
    allowed_domains = ['cars-data.com']
    start_urls = ['http://cars-data.com/en/audi-a5-sportback-1.4-tfsi-150hp-specs/%d' % x for x in xrange(1,10)]

    def parse(self, response):
        car = CarscraperItem()
        car['name'] = response.css("h1::text").extract_first()
        # = response.css("h1::text").extract_first()
        # sloppy,but no intense thought needed if they're always in the same spot.
        # just testing this out for now
        # if it works it stays
        car['power'] = response.css(".col-7 > div:nth-child(3) > div:nth-child(15)::text").extract_first()
        car['maxPowerRpm'] = response.css(".col-7 > div:nth-child(3) > div:nth-child(13)::text").extract_first()
        car['torque'] = response.css(".col-7 > div:nth-child(3) > div:nth-child(17)::text").extract_first()
        car['maxTorqueRpm'] = response.css(".col-7 > div:nth-child(3) > div:nth-child(19)::text").extract_first()
        yield car # send to pipeline for use 
