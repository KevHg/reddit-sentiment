# Reddit NLP Sentiment
Analytics tool of positive / negative sentiment of Reddit posts and comments, given a subreddit and a keyword.

## Status
Partially completed. Main functions are working, but sentiment analysis could be much more sensible, e.g. applying upvote multiplier based on the subreddit's usual activity.

Also it'll look much nicer if it comes with a UI!

## tl;dr - How it works
1) Specify search term and which subreddit to perform the analytics on
2) Begin web scraping of top search result links, looking through all comments of each post
3) Clean each comment text with NLTK and calculate its sentiment score with Vader
4) Augment each comment's score with the upvote count
5) Return average sentiment score
