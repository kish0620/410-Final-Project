from flask import Flask, render_template, request, jsonify

import praw
from textblob import TextBlob

from collections import OrderedDict


app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html', objective_subjective_dict = {})

@app.route('/hot-posts', methods=['POST'])
def reddit_page():
    reddit = praw.Reddit(client_id='AEKarPyPLIRaMiW5K9mjaQ', client_secret='YodD2MDeah332hCK1GhIpCSd4Zq2oA', user_agent='410 Project')
    subreddit = request.get_json()['data']
    hot_posts = reddit.subreddit(subreddit).controversial(limit=None)
    sentiment_dict = OrderedDict()
    sentiment_dict['[-1, -0.6)'] = 0
    sentiment_dict['[-0.6, -0.4)'] = 0
    sentiment_dict['[-0.4, -0.2)'] = 0
    sentiment_dict['[-0.2, 0)'] = 0
    sentiment_dict['(0, 0.2)'] = 0
    sentiment_dict['[0.2, 0.4)'] = 0
    sentiment_dict['[0.4, 0.6)'] = 0
    sentiment_dict['[0.6, 1)'] = 0
    objective_subjective_dict = {}
    objective_subjective_dict['objective'] = 0
    objective_subjective_dict['subjective'] = 0
    for post in hot_posts:
        score = float(TextBlob(post.title).sentiment.polarity)
        if score < -0.6:
            sentiment_dict['[-1, -0.6)'] += 1
        elif score >= -0.6 and score < -0.4:
            sentiment_dict['[-0.6, -0.4)'] += 1
        elif score >= -0.4 and score < -0.2:
            sentiment_dict['[-0.4, -0.2)'] += 1
        elif score >= -0.2 and score < 0:
            sentiment_dict['[-0.2, 0)'] += 1
        elif score > 0 and score < 0.2:
            sentiment_dict['(0, 0.2)'] += 1
        elif score >= 0.2 and score < 0.4:
            sentiment_dict['[0.2, 0.4)'] += 1
        elif score >= 0.4 and score < 0.6:
            sentiment_dict['[0.4, 0.6)'] += 1
        elif score >= 0.6:
            sentiment_dict['[0.6, 1)'] += 1
        
        if score == 0.0:
            objective_subjective_dict['objective'] += 1
        else:
            objective_subjective_dict['subjective'] += 1

    return jsonify({
        'sentiment_dict': sentiment_dict, 
        'obj_subj_dict': objective_subjective_dict
    })

if __name__ == "__main__":
    app.run()