import requests
from requests_oauthlib import OAuth1
import sys

API_KEY = ""
API_KEY_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
API_URL = "https://api.twitter.com/2/tweets"


def tweet_text(tweet_output):
    oauth = OAuth1(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    response = requests.post(API_URL, json={"text": tweet_output}, auth=oauth)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tweet_script.py <tweet_text>")
        sys.exit(1)

    tweet_output = sys.argv[1]
    tweet_text(tweet_output)
