import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import RedditPost


class RedditPostScraper(CrawlSpider):
    name = 'reddit-posts'

    def __init__(self, domain='', *args, **kwargs):
        super(CrawlSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = ['old.reddit.com']
        self.start_urls = [domain]
        # start_urls = ['https://www.google.com/search?as_sitesearch=reddit.com/r/MouseReview&q=g305']

    rules = (
        Rule(LinkExtractor(allow=('/comments/',)), callback='parse_item'),
    )

    def parse_item(self, response):
        yield {
            'title': response.css('a[data-event-action=title]::text').get(),
            # 'comments': response.css('div[class=md] p::text').getall(),

            'comments': response.css('div.commentarea div.entry.unvoted \
            div.usertext-body.may-blank-within.md-container div.md p::text').getall(),

            'upvotes': response.css('span.score.unvoted::text').getall()
            # 'upvotes': response.xpath("//*[contains(text(), 'points')]").getall()
        }


