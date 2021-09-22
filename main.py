import os
import praw
from flask import Flask, jsonify

"""
This API has been created by yash vardhan, to use in "project-memeit".
This API is private and not meant to be use publicly in any other project.
Illegal copying of this code is an offence and punishable under the law.
"""

app = Flask(__name__)
reddit = praw.Reddit(client_id='2roma39k4b7nKeLdK4vtTQ',
                     client_secret='wnNaoA1-kcefBJEgwJyLkEKQ0tdG3w', password='GajarKaHalwa1947',
                     user_agent='PrawTut', username='MemeitOfficial')


@app.route('/<string:n>')
def userInput(n):
    try:
        subreddit = reddit.subreddit(n)
        Main_Output = subreddit.hot(limit=50)
        MainArray = []
        for submissions in Main_Output:
            meme = submissions.url
            title = submissions.title
            extension = meme[len(meme) - 3:].lower()
            if "jpg" in extension or "png" in extension or "gif" in extension:
                _ = submissions.preview
                result = {
                    "subreddit": n,
                    "title": title,
                    "url": meme
                }
                MainArray.append(result)
        finalResult = {
            "code": 200,
            "count": 50,
            "memes": MainArray
        }

        return jsonify(finalResult)
    except Exception as e:

        return {
            "code": 400,
            "message": str(type(e)) + str(e),
            "help": "Subreddit Doesn't Exist, Check if u spelled it correctly.."
        }


@app.route('/<string:topic>/<int:num>')
def VideoUserInput(topic, num):
    try:
        subreddit = reddit.subreddit(topic)
        Main_Output = subreddit.hot(limit=num)
        MainArray = []
        for submissions in Main_Output:
            meme = submissions.url
            title = submissions.title
            vid_extension = meme[:9]
            if "https://v" in vid_extension:
                _ = submissions.preview
                result = {
                    "audio_url": meme + "/DASH_audio.mp4",
                    "subreddit": topic,
                    "title": title,
                    "url": meme + "/DASH_360.mp4"
                }
                MainArray.append(result)
        finalResult = {
            "code": 200,
            "count": num,
            "memes": MainArray
        }

        return jsonify(finalResult)
    except Exception as e:

        return {
            "code": 400,
            "message": str(type(e)) + str(e),
            "help": "Subreddit Doesn't Exist, Check if u spelled it correctly.."
        }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.debug = True
    app.run(port=port)
