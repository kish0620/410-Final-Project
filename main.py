from flask import Flask, render_template, jsonify
import tweepy

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/profile/')
def profile_page():
    client = tweepy.Client("H5QGYLFwtmrezKTXKvIBER8UE")
    public_tweets = client.get_home_timeline()
    tweets = []
    for tweet in public_tweets:
        tweets.append(tweet.text)
    return jsonify(tweets)