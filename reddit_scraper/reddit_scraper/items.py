import scrapy


class RedditPost(scrapy.Item):
    title = scrapy.Field()
    comments = scrapy.Field()
    upvotes = scrapy.Field()


