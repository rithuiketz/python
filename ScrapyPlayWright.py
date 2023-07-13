from scrapy.crawler import CrawlerProcess
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        url = 'https://www.tesco.com/groceries/en-GB/products/288608322'
        yield scrapy.Request(url, meta=dict(
            playwright = True,
            playwright_include_page = True, 
            errback=self.errback,
        ))

    async def parse(self, response):
        print("Called")
        print(response.css('a').extract())
        yield None
        #print(response)
        #page = response.meta["playwright_page"]
        #await page.close()

        #for quote in response.css('div.quote'):
            #quote_item = QuoteItem()
            #quote_item['text'] = quote.css('span.text::text').get()
            #quote_item['author'] = quote.css('small.author::text').get()
            #quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            #yield quote.css('span.text::text').get()
  
    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
    
process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()