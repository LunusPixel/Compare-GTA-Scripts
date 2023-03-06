from urllib import request
import hashlib
import os
import time
import tweepy

# Twitter API keys and access tokens
CONSUMER_KEY = "your_consumer_key"
CONSUMER_SECRET = "your_consumer_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

CHECK_INTERVAL = 1  # Minutes
FILE_NAME = "bg_ng_944_1.rpf"
OLD_MD5_FILE_PATH = os.path.abspath("old.txt")
FILE_KEY = "F06F12F49B843DADE4A7BE053505B19C9E415C95D93753450A269144D59A0115"
FILE_URL = "http://prod.cloud.rockstargames.com/titles/gta5/pcros/bgscripts/bg_ng_944_1.rpf"

# Authenticate Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

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

        # If file is updated, write new MD5 to file and tweet about it
        print("Comparing MD5s...")
        if old_md5 != new_md5:
            print(f"{FILE_NAME} updated!")
            with open(OLD_MD5_FILE_PATH, "w") as fp:
                fp.write(new_md5)

            # Tweet about the update
            tweet_text = f"🚨 {FILE_NAME} has been updated! 🚨"
            api.update_status(tweet_text)

        else:
            print("No changes found!")

        # Sleep until next try
        print(f"Sleeping for {CHECK_INTERVAL} minute(s)...\n")
        time.sleep(60 * CHECK_INTERVAL)

except Exception as e:
    print(f"Error occurred: {str(e)}")
