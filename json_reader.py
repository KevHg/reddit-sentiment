import json
import os
from collections import namedtuple


# class RedditPost(object):
#     def __init__(self, title, comments, upvotes):
#         self.title = title
#         self.comments = comments
#         self.upvotes = upvotes




path = os.path.join('reddit_scraper', 'reddit.jl')

with open(path) as f:
    for line in f:
        post = json.loads(line)
        print(post['title'])
        print(len(post['comments']))
        print(len(post['upvotes']))



        # post = json.loads()


# user = json.loads('{"__type__": "User", "name": "John Smith", "username": "jsmith"}')
