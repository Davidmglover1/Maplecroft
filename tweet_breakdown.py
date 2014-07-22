def tweet_breakdown(tweet_list, user_tweets_list):
	for item in user_tweets_list:
		midstr = item.replace("#", "")
		midstr = midstr.replace(":", " ")
		finstr = midstr.replace("'", " ")
		tweet_list.append(finstr.split())