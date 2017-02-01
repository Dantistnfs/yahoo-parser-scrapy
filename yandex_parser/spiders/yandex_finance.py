# -*- coding: utf-8 -*-
import scrapy
from yandex_parser.items import YandexParserItem
import padnas

class YandexFinanceSpider(scrapy.Spider):
	name = "yandex-finance"
	allowed_domains = ["finance.yahoo.com"]
	start_urls = ['https://finance.yahoo.com/quote/EA']

	def parse(self, response):
		item = YandexParserItem()
		item['name'] = response.url.split("/")[-1]
		item['current_price'] = response.xpath("//span[@class='Fw(b) Fz(36px) Mb(-4px)']/text()").extract()[0]

		data = response.xpath("//td[@class='Ta(end) Fw(b)']")
		for data_line in data:
			data_name = data_line.xpath("@data-test").extract()[0].split('-')[0]
			item[data_name] = data_line.xpath("text()").extract()[0]

		yield item
