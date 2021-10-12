"""
This API has been created by yash vardhan, to use in "project-memeit".
This API is private and not meant to be use publicly in any other project.
Illegal copying of this code is an offence and punishable under the law.
happily created with love...
"""
import os
import random
import praw
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
reddit = praw.Reddit(client_id=os.getenv("client_id"),
                     client_secret=os.getenv("client_secret"), password=os.getenv("password"),
                     user_agent=os.getenv("user_agent"), username=os.getenv("username"))


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
        print(e)
        randomArray = ["AdviceAnimals",
                       "MemeEconomy",
                       "IndianDankMemes",
                       "terriblefacebookmemes",
                       "ComedyCentral",
                       "me_irl",
                       "dankmemes"]
        x = random.choice(randomArray)
        subreddit = reddit.subreddit(x)
        Main_Output = subreddit.hot(limit=50)
        MainArray = []
        for submissions in Main_Output:
            meme = submissions.url
            title = submissions.title
            extension = meme[len(meme) - 3:].lower()
            if "jpg" in extension or "png" in extension or "gif" in extension:
                _ = submissions.preview
                result = {
                    "subreddit": x,
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

        finalVideoResult = {
            "code": 200,
            "count": num,
            "memes": MainArray
        }

        return jsonify(finalVideoResult)

    except Exception as e:
        randomVideoArray = ["teenagers", "IndianMeyMeys",
                            "indiameme", "memes", "MemeEconomy", "IndianDankMemes",
                            "terriblefacebookmemes", "ComedyCentral", "me_irl", "funny", "PewdiepieSubmissions"]
        y = random.choice(randomVideoArray)
        subreddit = reddit.subreddit(y)
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
                    "subreddit": y,
                    "title": title,
                    "url": meme + "/DASH_360.mp4"
                }
                MainArray.append(result)

        finalVideoResult = {
            "code": 200,
            "count": num,
            "memes": MainArray
        }

        print(e)
        return jsonify(finalVideoResult)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.debug = True
    app.run(port=port)
