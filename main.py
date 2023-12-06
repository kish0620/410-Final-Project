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
        consumer_key="API/oK5hQ5rZn6hvNqR6c1QwD8Xe5",
        consumer_secret="API/fhG11tIKBs2wL1NynfoO5dgJUTZVQiOtZ1smjTXzuwBCpSjaBQ",
        access_token="1428502636379181061-oKVo2k0yOD8w4LVSs7gZpeA3w5Xrwi",
        access_token_secret="HP6490J7ktBXTb1fH7xafhZhlWlt2VjZnbYXMBw2edOC1"
    )
    # print(client.consumer_key)
    public_tweets = client.search_all_tweets()
    tweets = []
    for tweet in public_tweets:
        tweets.append(tweet.text)
    return jsonify(tweets)

if __name__ == "__main__":
    # main_page()
    app.run()