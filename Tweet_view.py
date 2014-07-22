from twython import Twython
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import datetime, os
from Model import MyCsvModel
from search_tweet import search_tweet
from tweet_breakdown import tweet_breakdown

def test (request):

	# Authorize Twitter OAuth2
	APP_KEY = 'DM2Mosw5Em6RKOYZCGDfypY8O'
	APP_SECRET = '43Vfes8sjge7oyTPHXxhVR6ayiG9iVAlEgUqtle7MuUfOrU50U'
	
	twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
	ACCESS_TOKEN = twitter.obtain_access_token()
	# https://twython.readthedocs.org/en/latest/usage/starting_out.html
	
	twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)	
	
	#Receive tweets
	user_tweets = twitter.get_user_timeline(screen_name='MaplecroftRisk', count = 10)
	user_tweets_list=[]
	
	# Create a list of tweet text
	for tweet in user_tweets:
		user_tweets_list.append(tweet['text'])
	
	#Import Data
	my_csv_list = MyCsvModel.import_data(data = open(os.path.join(os.path.dirname(__file__), 'countries.csv').replace('\\','/')))
	
	# Display all 10 tweets
	now = datetime.datetime.now()
	tweet_1 = user_tweets_list[0]
	tweet_2 = user_tweets_list[1]
	tweet_3 = user_tweets_list[2]
	tweet_4 = user_tweets_list[3]
	tweet_5 = user_tweets_list[4]
	tweet_6 = user_tweets_list[5]
	tweet_7 = user_tweets_list[6]
	tweet_8 = user_tweets_list[7]
	tweet_9 = user_tweets_list[8]
	tweet_10 = user_tweets_list[9]
	
	# Remove hash-tags and tokenize the tweet strings
	tweet_list = []
	tweet_breakdown(tweet_list, user_tweets_list)

	# mapped_country is a list of countries to be mapped; needs to be edited in search_tweet to remove .country line 6
	mapped_country = []
	search_tweet(tweet_list, my_csv_list, mapped_country)
	
	return render(request, 'Tweets.html', {'current_date': now, 'tweet_1': tweet_1, 'tweet_2': tweet_2, 'tweet_3': tweet_3, 'tweet_4': tweet_4, 'tweet_5': tweet_5, 'tweet_6': tweet_6, 'tweet_7': tweet_7, 'tweet_8': tweet_8, 'tweet_9': tweet_9, 'tweet_10': tweet_10, 'mapped_country': mapped_country})