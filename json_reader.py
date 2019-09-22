import json
import os
from collections import namedtuple


class RedditPost():
    def __init__(self, title, comments):
        self.title = title
        self.comments = comments


class RedditComment():
    def __init__(self, text, upvotes):
        self.text = text
        self.upvotes = upvotes


def convert_json(filename):
    path = os.path.join('reddit_scraper', filename)
    posts = []
    with open(path) as f:
        for line in f:
            post = json.loads(line)
            title = post['title']
            comment_texts = post['comments']
            upvotes = post['upvotes']
            comments = []
            for i in range(len(upvotes)):
                comment = RedditComment(comment_texts[i], upvotes[i])
                comments.append(comment)
            post = RedditPost(title, comments)
            posts.append(post)

    return posts

    # for post in posts:
    #     print(post.title)
    #     for comment in post.comments:
    #         print(comment.text, comment.upvotes)


