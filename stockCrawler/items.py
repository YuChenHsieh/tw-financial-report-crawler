# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FinancialReportItem(scrapy.Item):
    title = scrapy.Field()
    year = scrapy.Field()
    season = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()

    # save all value in a dictionary
    balance = scrapy.Field()
    income = scrapy.Field()
    cash = scrapy.Field()

    pass


class StockSymbolItem(scrapy.Item):
    sheet = scrapy.Field()

    pass
