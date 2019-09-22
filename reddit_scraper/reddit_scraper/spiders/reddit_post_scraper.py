import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import RedditPost


class RedditPostScraper(CrawlSpider):
    name = 'reddit-posts'
    allowed_domains = ['old.reddit.com']

    start_urls = ['https://old.reddit.com/r/MouseReview/']
    # start_urls = ['https://www.google.com/search?as_sitesearch=reddit.com/r/MouseReview&q=g305']

    rules = (
        Rule(LinkExtractor(allow=('/comments/',)), callback='parse_item'),
    )

    def parse_item(self, response):
        # self.logger.info(f'Crawling into {response.url}')
        # item = RedditPost()
        # item.title = response.css('h1::text').get()
        # item.comments = response.css('div[data-test-id=comment] div p::text').getall()
        # item.upvotes = response.xpath("//*[contains(text(), 'points')]").getall()
        #
        # return item

        yield {
            'title': response.css('a[data-event-action=title]::text').get(),
            # 'comments': response.css('div[class=md] p::text').getall(),

            'comments': response.css('form.usertext.warn-on-unload div.usertext-body.may-blank-within.md-container div.md p::text').getall(),

            'upvotes': response.css('span.score.unvoted::text').getall()
            # 'upvotes': response.xpath("//*[contains(text(), 'points')]").getall()
        }


