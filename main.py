from flask import Flask, render_template, jsonify
import tweepy

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/profile/')
def profile_page():
    # client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAACFerAEAAAAAGZ1TtfAH%2BnvkvR%2Fo4Sp0dGBFvTo%3DdZrPu6tRB4gH70qMYaw4tvWWNfVrX0V5hH1LPKoZpJH2a9yeaD")
    client = tweepy.Client(
        consumer_key="API/kSXIgzEy4k18JChvTHVEEioBQ",
        consumer_secret="API/qOsOMGIcccIeKKINKu9nAVzGeJ8rdj4Be2gP4A85iQOEgLTQZE",
        access_token="1428502636379181061-OS1j4TfmzTVZvue5eP32k207GOHWeL",
        access_token_secret="I3lfHDaEsClowmwkUIK29Zg1WWRFiwOdDsj8gRGfW2bDh"
    )
    # print(client.consumer_key)
    public_tweets = client.get_blocked()
    tweets = []
    for tweet in public_tweets:
        tweets.append(tweet.text)
    return jsonify(tweets)

if __name__ == "__main__":
    # main_page()
    app.run()