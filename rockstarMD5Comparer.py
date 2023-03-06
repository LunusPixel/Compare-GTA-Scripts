from urllib import request
import hashlib
import os
import time
import tweepy
import requests

# Set constants
CHECK_INTERVAL = 1  # Minutes
FILE_NAME = "bg_ng_944_1.rpf"
OLD_MD5_FILE_PATH = os.path.abspath("old.txt")
FILE_KEY = "F06F12F49B843DADE4A7BE053505B19C9E415C95D93753450A269144D59A0115"
FILE_URL = "http://prod.cloud.rockstargames.com/titles/gta5/pcros/bgscripts/bg_ng_944_1.rpf"

# Set credentials for Twitter API and Discord webhook
twitter_credentials = {
    "consumer_key": "your_consumer_key",
    "consumer_secret": "your_consumer_secret",
    "access_token": "your_access_token",
    "access_token_secret": "your_access_token_secret"
}
discord_webhook_url = "your_discord_webhook_url"

# Authenticate Twitter API and create API object
auth = tweepy.OAuthHandler(twitter_credentials["consumer_key"], twitter_credentials["consumer_secret"])
auth.set_access_token(twitter_credentials["access_token"], twitter_credentials["access_token_secret"])
twitter_api = tweepy.API(auth)

# Define function to send notification to Discord webhook
def send_discord_notification(webhook_url, message):
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        print(f"Failed to send Discord notification. Status code: {response.status_code}")

try:
    while True:
        # Download new file and get its MD5
        print(f"Downloading new {FILE_NAME}...")
        with request.urlopen(FILE_URL) as response, open(FILE_NAME, "wb") as file:
            data = response.read()
            file.write(data)
            new_md5 = hashlib.md5(data).hexdigest()

        # Read old MD5 from file
        print("Reading old MD5...")
        with open(OLD_MD5_FILE_PATH, "r") as fp:
            old_md5 = fp.readline()

        # If file is updated, write new MD5 to file and send notifications
        print("Comparing MD5s...")
        if old_md5 != new_md5:
            print(f"{FILE_NAME} updated!")
            with open(OLD_MD5_FILE_PATH, "w") as fp:
                fp.write(new_md5)

            # Send tweet about the update
            tweet_text = f"🚨 {FILE_NAME} has been updated! 🚨"
            twitter_api.update_status(tweet_text)

            # Send Discord notification about the update
            discord_notification_text = f"**{FILE_NAME} has been updated!**"
            send_discord_notification(discord_webhook_url, discord_notification_text)

        else:
            print("No changes found!")

        # Sleep until next try
        print(f"Sleeping for {CHECK_INTERVAL} minute(s)...\n")
        time.sleep(60 * CHECK_INTERVAL)

except Exception as e:
    print(f"Error occurred: {str(e)}")
