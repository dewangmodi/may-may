import praw
from praw.models import MoreComments
import regex
import datetime
import mysql.connector
import os

#We try to connect to database
#If it fails, we create one
try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="maymay",
      passwd=os.getenv("db_password"),
      database="maymayurls"
    )
    mycursor = mydb.cursor()
except:
    mydb = mysql.connector.connect(
      host="localhost",
      user="maymay",
      passwd=os.getenv("db_password")
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE maymayurls")
    mycursor.execute("CREATE TABLE urls (url VARCHAR(255))")

#Need to enter your own details
r = praw.Reddit(client_id=os.getenv("reddit_id"),
                     client_secret=os.getenv("reddit_secret"),
                     password=os.getenv("reddit_password"),
                     user_agent='using praw',
                     username=os.getenv("reddit_username")) 

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

#Adding links to database
for post in dict["url"]:
    sql = 'INSERT INTO urls VALUES ("%s")'
    mycursor.execute(sql % post)
    print("Entered",post,"to database")   

#Closing
mydb.commit()
mycursor.close()
mydb.close()