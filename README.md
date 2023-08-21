# Twitter API Scripts

This repository contains simple scripts that allow you to interact with the Twitter API to post text tweets and tweets with images.

## Getting started

### Twitter API Setup
Before you can use these scripts, you need to set up a Twitter Developer account and create an application to obtain API keys and secrets. Follow these steps to get your credentials:

#### Create a Twitter Developer Account:
If you don't already have a Twitter Developer account, go to the Twitter Developer Portal and sign up.

#### Create a New Twitter App:
Once you're logged in, click on the "Projects & Apps" tab.
Click the "Create App" button and fill in the necessary information.
After creating the app, navigate to the "Keys and tokens" tab to find your API keys and secrets.
#### Add Keys to Scripts:
In the script files (tweet_text.py and tweet_image.py), replace the placeholders:
- YOUR_API_KEY, 
- YOUR_API_SECRET, 
- YOUR_ACCESS_TOKEN, 
- YOUR_ACCESS_SECRET 

with the actual keys and tokens obtained from the Twitter Developer Portal.

## Installing Dependencies
To run the scripts, you need to have Python and few libraries installed. If you haven't installed it yet, you can do so using the following command:
```bash
pip install tweepy requests_oauthlib requests
```
** To use script only for tweeting text you don't need to install tweepy. Tweepy will be helpful with posting images on twitter.

## Using the Scripts

### Tweeting Text Posts
To tweet a text post using the tweet_text.py script, follow these steps:

Open a terminal and navigate to the project directory.
Run the script with the following command:
```bash
python tweet_text.py "Your text here"
```
Replace "Your text here" with the text you want to tweet.

### Tweeting Posts with Images
To tweet an image along with a text caption using the tweet_image.py script, follow these steps:

Place the image you want to tweet in the images directory.
Open a terminal and navigate to the project directory.
Run the script with the following command:
```bash
python tweet_image.py images/your_image_filename.jpg "Your caption here"
```
Replace "Your caption here" with your desired caption and images/your_image_filename.jpg with the actual path to your image file.