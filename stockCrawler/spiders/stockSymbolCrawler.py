import scrapy
from stockCrawler.items import StockSymbolItem
from utils.formatting import normalize, num


class StockSymbolSpider(scrapy.Spider):
    name = 'stockSymbolCrawler'
    allowed_domains = ['isin.twse.com.tw']

    url = 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
    start_urls = [url]

    def parse(self, response):  # crawler logic
        items = StockSymbolItem()

        sheet = response.xpath(
            "//table[2]/tr"
        )
        sheetValue = []

        for row in sheet[2:]:
            col1 = row.xpath('./td[1]/text()').get()

            if(col1 == None):
                continue

            symbol = col1.split('\u3000')[0]
            name = col1.split('\u3000')[1]
            industry = row.xpath('./td[5]/text()').get()

            sheetValue.append(
                dict([('symbol', symbol), ('name', name), ('industry', industry)]))

        items['sheet'] = sheetValue
        return items
