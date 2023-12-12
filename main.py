from flask import Flask, render_template, jsonify
import tweepy

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import praw
from textblob import TextBlob
import datetime

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/hot-posts/')
def reddit_page():
    print(TextBlob("This is really stupid").sentiment)
    reddit = praw.Reddit(client_id='AEKarPyPLIRaMiW5K9mjaQ', client_secret='YodD2MDeah332hCK1GhIpCSd4Zq2oA', user_agent='410 Project')
    hot_posts = reddit.subreddit('politics').controversial(limit=None)
    posts = []
    posts.append('10 hottest machine learning subreddit posts')
    for post in hot_posts:
        # print(datetime.datetime.fromtimestamp(post.created_utc))
        # print(post.title)
        posts.append(post.title)
        score = TextBlob(post.title)
        print(score.sentiment)
    # return jsonify(posts)
    return render_template('index.html', posts=posts)
    # # Downloading imdb top 250 movie's data
    # url = 'http://www.imdb.com/chart/top'
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    # movies = soup.select('td.titleColumn')
    # crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    # ratings = [b.attrs.get('data-value')
    #         for b in soup.select('td.posterColumn span[name=ir]')]
    
    
    
    
    # # create a empty list for storing
    # # movie information
    # movie_list = []
    
    # # Iterating over movies to extract
    # # each movie's details
    # for index in range(0, len(movies)):
        
    #     # Separating movie into: 'place',
    #     # 'title', 'year'
    #     movie_string = movies[index].get_text()
    #     print(movie_string)
    #     movie = (' '.join(movie_string.split()).replace('.', ''))
    #     movie_title = movie[len(str(index))+1:-7]
    #     year = re.search('\((.*?)\)', movie_string).group(1)
    #     place = movie[:len(str(index))-(len(movie))]
    #     data = {"place": place,
    #             "movie_title": movie_title,
    #             "rating": ratings[index],
    #             "year": year,
    #             "star_cast": crew[index],
    #             }
    #     movie_list.append(data)
    # return jsonify(movie_list)
    # # client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAACFerAEAAAAAGZ1TtfAH%2BnvkvR%2Fo4Sp0dGBFvTo%3DdZrPu6tRB4gH70qMYaw4tvWWNfVrX0V5hH1LPKoZpJH2a9yeaD")
    # client = tweepy.Client(
    #     # bearer_token="AAAAAAAAAAAAAAAAAAAAACFerAEAAAAAMC8z%2Fubdv%2F6P2JccfB%2BexrhmXRc%3DcnKnmuFuKEmy2V6mQPLFNK6KrkCPocjO3uXEY1h5LlCdkvSQ8F",
    #     consumer_key="API/kSXIgzEy4k18JChvTHVEEioBQ",
    #     consumer_secret="API/qOsOMGIcccIeKKINKu9nAVzGeJ8rdj4Be2gP4A85iQOEgLTQZE",
    #     access_token="1428502636379181061-OS1j4TfmzTVZvue5eP32k207GOHWeL",
    #     access_token_secret="I3lfHDaEsClowmwkUIK29Zg1WWRFiwOdDsj8gRGfW2bDh"
    # )
    # # print(client.consumer_key)
    # # username = client.account()
    # public_tweets = client.get_home_timeline()
    # # tweets = []
    # # for tweet in public_tweets:
    # #     tweets.append(tweet.text)
    # # api = TwitterAPI("API/kSXIgzEy4k18JChvTHVEEioBQ", "API/qOsOMGIcccIeKKINKu9nAVzGeJ8rdj4Be2gP4A85iQOEgLTQZE", "1428502636379181061-OS1j4TfmzTVZvue5eP32k207GOHWeL", "I3lfHDaEsClowmwkUIK29Zg1WWRFiwOdDsj8gRGfW2bDh", api_version='2')
    # # r = api.request('tweets/search/recent', {
    # #         'query':'pizza',
    # #         'tweet.fields':'author_id',
    # #         'expansions':'author_id'})
    # # for item in r:
    # #         print(item)
    # # return jsonify(r)

if __name__ == "__main__":
    # main_page()
    app.run()