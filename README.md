# Reddit NLP Sentiment
Analytics tool of positive / negative sentiment of Reddit posts and comments, given a subreddit and a keyword.

#### Why Reddit?

A massive forum of information, with dedicated subreddits for almost anything you can think of. Plus, it also features voting system, meaning we can distinguish between well-thought opinions against poor ones.

I like to browse Reddit to read up the general opinion on a certain subject, e.g. whether a certain keyboard model is good or not. But why do it yourself when you can automate it, right?



## How it's supposed to work
1) Specify search term and which subreddit to perform the analytics on
2) Begin web scraping on several pages, looking through all comments of each post
3) Get sentiment score (positivity vs negativity) of each comment with NLP (Vader)
4) Augment sentiment score by the comment's upvote count
5) Return average score and top occurring keywords of all comments



## Workflow
* Web scraping
    * Post title and list of comments  - **Done!**
    * Upvote count - **Done!**
    * Query arguments instead of hardcoded URL - **Done!**
    * Execute spider from python script - ***Done!***
* Sentiment score
    * Look into Vader from NLTK - ***In progress***
    * Test out sentiment score results
    * Apply upvote multiplier, potentially non-linear
* Integration
    * Script scrapy crawl with sentiment score calculation
    * Get top occurring keywords
* Bonus
    * UI instead of terminal
