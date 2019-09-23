# Reddit NLP Sentiment
Analytics tool of positive / negative sentiment of Reddit posts and comments, given a subreddit and a keyword.

#### Why Reddit?
A massive forum of information, with dedicated subreddits for almost anything you can think of. Plus, it also features voting system, meaning we can distinguish between well-thought opinions against poor ones.

I like to browse Reddit to read up the general opinion on a certain subject, e.g. whether a certain keyboard model is good or not. But why do it yourself when you can automate it, right?

## Status
Partially completed. Main functions working, but finer issues need to be resolved.

## tl;dr - How it works
1) Specify search term and which subreddit to perform the analytics on
2) Begin web scraping of top search result links, looking through all comments of each post
3) Clean each comment text with NLTK and calculate its sentiment score with Vader
4) Augment each comment's score with the upvote count
5) Return average sentiment score

## Current Issues
* How to standardize the upvote multiplier? Different subreddits have different upvote activity
    * *Normalize* - Cannot handle situation where there are very few negative sentiments
    * *Weighting* - Cannot handle situation where most comments have equally low upvote count
* Is Vader good enough for more precise sentiment analysis?
    * Look into NLP

## Workflow
* Web scraping
    * Post title and list of comments  - **Done!**
    * Upvote count - **Done!**
    * Query arguments instead of hardcoded URL - **Done!**
    * Execute spider from python script - **Done!**
* Sentiment score
    * Look into Vader from NLTK - **Done!**
    * Test out sentiment score results - **Done!**
    * Apply upvote multiplier, potentially non-linear - ***In progress***
* Integration
    * Script scrapy crawl with sentiment score calculation - **Done!**
    * Get top occurring keywords
* Bonus
    * UI instead of terminal
