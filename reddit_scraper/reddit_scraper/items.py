import scrapy


class RedditPost(scrapy.Item):
    title = scrapy.Field()


