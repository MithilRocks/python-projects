import tweepy
from textblob import TextBlob
import pprint

consumer_key = '51wBiPvylKUPsbeGrNjXyAOqm'
consumer_secret = 'hongDDNipHxkOPv3sVtViodEvR8ddMiLtpVnx7ztzQEZc8z1GM'

access_token = '132166898-04fqAhYKgAM2JiryOcrbtqz18o0pmzRJJ6iRb9E0'
access_token_secret = 'vGmGwoXKxiEozvJmnO6gwhGfPPuo4V1uo2LT3ydMD5FKs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Trump")

print(len(public_tweets))
