import os
from scrapy.crawler import CrawlerProcess
import pandas as pd

import json_reader
from sentiment_score import calculate_sentiment_score
from reddit_scraper.reddit_scraper.spiders.reddit_post_scraper import RedditPostCrawler

if __name__ == '__main__':
    # Ask for user query
    subreddit = input('Subreddit: ')
    term = input('Search term: ')
    term = term.replace(' ', '+')

    # Start crawler process
    print('[LOG] Crawling Reddit, this will take some time...')
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'jl',
        'FEED_URI': 'data.jl'
    })
    process.crawl(RedditPostCrawler,
                  domain=f'https://old.reddit.com/r/{subreddit}/search?q={term}&sort=relevance&t=all')
    process.start()

    # Convert data file to class
    print('[LOG]: Creating DataFrame table')
    reddit_posts = json_reader.convert_json('data.jl')
    all_comments = []
    all_upvotes = []

    for post in reddit_posts:
        for comment in post.comments:
            all_comments.append(comment.text)
            upvote = comment.upvotes.split(' ')[0]
            all_upvotes.append(int(upvote))

    df = pd.DataFrame({'comment':all_comments, 'upvotes': all_upvotes})
    df = df[df.upvotes >= 1]

    print('[LOG] Calculating sentiment score, this will take some more time...')
    df = calculate_sentiment_score(df)

    df.to_csv('results.csv')
    print('[LOG] Completed!\n')
    print('Average sentiment:', df.sentiment.mean())
    print('where +1 is most positive and -1 is most negative')

    os.remove('data.jl')
