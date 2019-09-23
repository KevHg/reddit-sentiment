import os
from scrapy.crawler import CrawlerProcess
import pandas as pd

import json_reader
from reddit_scraper.reddit_scraper.spiders.reddit_post_scraper import RedditPostCrawler

if __name__ == '__main__':

    # Ask for user query
    subreddit = input('Subreddit: ')
    term = input('Search term: ')
    term = term.replace(' ', '+')

    # Start crawler process
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'jl',
        'FEED_URI': 'data.jl'
    })
    process.crawl(RedditPostCrawler, domain=f'https://old.reddit.com/r/{subreddit}/search?q={term}&sort=relevance&t=all')
    process.start()

    # Convert data file to class
    reddit_posts = json_reader.convert_json('data.jl')

    all_comments = []
    all_upvotes = []

    for post in reddit_posts:
        for comment in post.comments:
            all_comments.append(comment.text)
            all_upvotes.append(comment.upvotes)

    df = pd.DataFrame({'comment':all_comments, 'upvotes': all_upvotes})
    print(df)

    os.remove('data.jl')
