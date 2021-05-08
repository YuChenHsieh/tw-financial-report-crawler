import scrapy
from stockCrawler.items import StockcrawlerItem
from utils.formatting import normalize, num


class StockCrawlerSpider(scrapy.Spider):
    name = 'stockCrawler'
    allowed_domains = ['mops.twse.com.tw']

    code = '1455'
    year = '2021'
    season = '1'
    url = f'https://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID={code}&SYEAR={year}&SSEASON={season}&REPORT_ID=C'
    start_urls = [url]

    items = StockcrawlerItem()

    def parse(self, response):  # crawler logic
        items = StockcrawlerItem()

        title = response.xpath("//div[@class='header']/div/span/text()").get()

        balanceSheet = response.xpath(
            "//div[@class='content']/table[1]/tr"
        )
        incomeSheet = response.xpath(
            "//div[@class='content']/table[2]/tr"
        )
        cashSheet = response.xpath(
            "//div[@class='content']/table[3]/tr"
        )

        balanceSheetValue = dict()
        incomeSheetValue = dict()
        cashSheetValue = dict()

        for row in balanceSheet:
            key = row.xpath('./td[1]/text()').get()  # '1220'
            name = row.xpath('./td[2]//text()').get()  # '本期所得稅資產'
            value = row.xpath('./td[3]//text()').getall()  # '58'

            if(key == None):
                continue

            value = num(''.join(value))
            balanceSheetValue[key] = dict(
                [('name', normalize(name)), ('value', value)])

        for row in incomeSheet:
            key = row.xpath('./td[1]/text()').get()  # '1220'
            name = row.xpath('./td[2]//text()').get()  # '本期所得稅資產'
            value = row.xpath('./td[3]//text()').getall()  # '58'

            if(key == None):
                continue

            value = num(''.join(value))
            incomeSheetValue[key] = dict(
                [('name', normalize(name)), ('value', value)])

        for row in cashSheet:
            key = row.xpath('./td[1]/text()').get()  # '1220'
            name = row.xpath(
                './td[2]//text()').get()  # '本期所得稅資產'
            value = row.xpath('./td[3]//text()').getall()  # '58'

            if(key == None):
                continue

            value = num(''.join(value))
            cashSheetValue[key] = dict(
                [('name', normalize(name)), ('value', value)])

        items['name'] = title.split(' ')[1]
        items['code'] = self.code
        items['year'] = self.year
        items['season'] = self.season
        items['income'] = incomeSheetValue
        items['cash'] = cashSheetValue
        items['balance'] = balanceSheetValue

        return items
