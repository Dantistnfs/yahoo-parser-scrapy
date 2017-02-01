# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YandexParserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    current_price = scrapy.Field()
    PREV_CLOSE = scrapy.Field()
    OPEN = scrapy.Field()
    BID = scrapy.Field()
    ASK = scrapy.Field()
    DAYS_RANGE = scrapy.Field()
    FIFTY_TWO_WK_RANGE = scrapy.Field()
    TD_VOLUME = scrapy.Field()
    AVERAGE_VOLUME_3MONTH = scrapy.Field()
    MARKET_CAP = scrapy.Field()
    BETA = scrapy.Field()
    PE_RATIO = scrapy.Field()
    EPS_RATIO = scrapy.Field()
    EARNINGS_DATE = scrapy.Field()
    DIVIDEND_AND_YIELD = scrapy.Field()
    EXDIVIDEND_DATE = scrapy.Field()
    ONE_YEAR_TARGET_PRICE = scrapy.Field()

    pass
