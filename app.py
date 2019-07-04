import praw
from praw.models import MoreComments
import regex
import datetime

r = praw.Reddit() 

subreddit = r.subreddit('memes')

memes=subreddit.new(limit=10)

subs = []
subCount = 0
sub_entries = {}


dict = { "title":[],
                "subreddit":[],
                "score":[], 
                "id":[], 
                "url":[], 
                "comms_num": [], 
                "created": [], 
                "body":[]}
for submission in memes:
    dict["title"].append(submission.title)
    dict['subreddit'].append(submission.subreddit)
    dict["score"].append(submission.score)
    dict["id"].append(submission.id)
    dict["url"].append(submission.url)
    dict["comms_num"].append(submission.num_comments)
    dict["created"].append(submission.created)
    dict["body"].append(submission.selftext)

for post in dict["url"]:
	print(post)