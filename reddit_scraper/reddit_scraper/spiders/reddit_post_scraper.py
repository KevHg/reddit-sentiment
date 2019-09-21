import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import RedditPost


class RedditPostScraper(CrawlSpider):
    name = 'reddit-posts'
    allowed_domains = ['reddit.com']
    start_urls = ['https://reddit.com/r/MouseReview/']

    rules = (
        Rule(LinkExtractor(allow=('/comments/',)), callback='parse_item'),
    )

    def parse_item(self, response):
        # self.logger.info(f'Crawling into {response.url}')
        # item = RedditPost()
        # item.url = str(response.url)
        # return item

        yield {
            'title': response.css('h1::text').get(),
            'data': response.css('div[data-test-id=comment] div p::text').getall()
        }


