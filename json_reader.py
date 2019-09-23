import json
import pandas as pd


class RedditPost():
    def __init__(self, title, comments):
        self.title = title
        self.comments = comments

    def to_dict(self):
        return {'title': [self.title] * len(self.comments),
                'comments': [c.text for c in self.comments], 'upvotes': [c.upvotes for c in self.comments]}


class RedditComment():
    def __init__(self, text, upvotes):
        self.text = text
        self.upvotes = upvotes


def convert_json(filename):
    posts = []
    with open(filename) as f:
        for line in f:
            post = json.loads(line)
            title = post['title']
            comment_texts = post['comments']
            upvotes = post['upvotes']
            comments = []
            for i in range(len(upvotes)):
                try:
                    comment = RedditComment(comment_texts[i], upvotes[i])
                    comments.append(comment)
                except IndexError:
                    break
            post = RedditPost(title, comments)
            posts.append(post)

    return posts


