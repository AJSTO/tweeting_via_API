import requests
import re
import sys
import tweepy
from requests_oauthlib import OAuth1

API_KEY = ""
API_KEY_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
API_URL = "https://api.twitter.com/2/tweets"

def tweet_image(image_path, caption):
    tweepy_auth = tweepy.OAuth1UserHandler(
        API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    )
    tweepy_api = tweepy.API(tweepy_auth)
    post = tweepy_api.simple_upload(image_path)
    text = str(post)
    media_id = re.search("media_id=(.+?),", text).group(1)
    payload = {
        "media": {"media_ids": [media_id]},
        "text": caption
    }

    oauth = OAuth1(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    response = requests.post(API_URL, json=payload, auth=oauth)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python tweet_image_script.py <image_path> <caption>")
        sys.exit(1)

    image_path = sys.argv[1]
    caption = sys.argv[2]
    tweet_image(image_path, caption)

