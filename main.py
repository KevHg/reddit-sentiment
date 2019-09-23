import os
from scrapy.crawler import CrawlerProcess
import pandas as pd
import logging
import nltk

import json_reader
from sentiment_score import clean_text, calculate_sentiment_score
from reddit_scraper.reddit_scraper.spiders.reddit_post_scraper import RedditPostCrawler

if __name__ == '__main__':
    # Initial setup: Disable scrapy logs and download NLTK files
    logging.getLogger('scrapy').propagate = False
    nltk.download('averaged_perceptron_tagger', quiet=True)
    nltk.download('wordnet', quiet=True)

    # Ask for user query
    subreddit = input('Subreddit: ')
    term = input('Search term: ')
    term = term.replace(' ', '+')

    # Start crawler process
    print('[LOG] Crawling Reddit, this will take a little time...')
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'jl',
        'FEED_URI': 'data.jl'
    })
    process.crawl(RedditPostCrawler,
                  domain=f'https://old.reddit.com/r/{subreddit}/search?q={term}&restrict_sr=on&sort=relevance&t=all')
    process.start()

    # Convert data file to class
    print('[LOG] Creating DataFrame table...')
    reddit_posts = json_reader.convert_json('data.jl')
    all_comments = []
    all_upvotes = []
    for post in reddit_posts:
        for comment in post.comments:
            all_comments.append(clean_text(comment.text))

            # Convert upvote text to float, e.g. '15.3k upvotes' -> 15300
            upvote = comment.upvotes.split(' ')[0]
            if 'k' in upvote:
                upvote = upvote[:-1]
                upvote = float(upvote) * 1000
            all_upvotes.append(float(upvote))

    df = pd.DataFrame({'comment': all_comments, 'upvotes': all_upvotes})
    df = df[df.upvotes >= 1]

    print('[LOG] Calculating sentiment score, this may take a longer time...')
    df = calculate_sentiment_score(df)

    # df.to_csv('results.csv')
    normalized_result = df.sentiment.mean()

    print('[LOG] Completed!\n')
    print('Average sentiment:', normalized_result)
    print('where +1 is most positive and -1 is most negative')

    os.remove('data.jl')
