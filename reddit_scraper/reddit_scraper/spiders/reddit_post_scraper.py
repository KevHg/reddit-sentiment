from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class RedditPostCrawler(CrawlSpider):
    """Crawler on Reddit posts given an 'old.reddit.com' domain, returning a title, list of comments,
    and list of upvotes"""
    name = 'reddit-posts'

    def __init__(self, domain='', *args, **kwargs):
        self.allowed_domains = ['old.reddit.com']
        self.start_urls = [domain]
        self.rules = (
            Rule(LinkExtractor(allow=('/comments/',)), callback='parse_item'),
        )

        super(RedditPostCrawler, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        yield {
            'title': response.css('a[data-event-action=title]::text').get(),
            # 'comments': response.css('div[class=md] p::text').getall(),

            'comments': response.css('div.commentarea div.entry.unvoted \
            div.usertext-body.may-blank-within.md-container div.md p::text').getall(),

            'upvotes': response.css('span.score.unvoted::text').getall()
            # 'upvotes': response.xpath("//*[contains(text(), 'points')]").getall()
        }
