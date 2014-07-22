def search_tweet(tweet_list, my_csv_list, mapped_country):
	for item in my_csv_list:
		count = 0
		while count < 10:
			if item.country in tweet_list[count]:
				mapped_country.append(item.country)
			count +=1			