import json
import os
from collections import namedtuple


# class RedditPost(object):
#     def __init__(self, title, comments, upvotes):
#         self.title = title
#         self.comments = comments
#         self.upvotes = upvotes




path = os.path.join('reddit_scraper', 'test.jl')

with open(path) as f:
    for line in f:
        post = json.loads(line)
        print(post['title'])
        c = post['comments']
        u = post['upvotes']
        for i in range(len(u)):
            print(c[i], u[i])



        # post = json.loads()


# user = json.loads('{"__type__": "User", "name": "John Smith", "username": "jsmith"}')
