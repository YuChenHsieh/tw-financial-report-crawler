# stock-crawler

### Env Setting
```
virtualenv --python=/usr/local/bin/python3 stock-crawler
source ./stock-crawler/bin/activate
```

### Quick Start
```
pip -r requirements.txt
# start stockSymbolCrawler
scrapy crawl stockSymbolCrawler -o test.json -t json -s FEED_EXPORT_ENCODING=utf-8
# start financialReportCrawler
scrapy crawl financialReportCrawler -o test.json -t json -s FEED_EXPORT_ENCODING=utf-8
```

### Setup DB (not yet)
```
docekr pull mongo
docker run --name mongo -p 27017:27017 -d
```

### Foler Structure
scrapy.cfg：基礎設置
items.py：抓取條目的結構定義
middlewares.py：中間件定義
pipelines.py：管道定義，用於抓取數據後的處理
settings.py：全局設置
spiders\stockCrawler.py：爬蟲主體，定義如何抓取需要的數據