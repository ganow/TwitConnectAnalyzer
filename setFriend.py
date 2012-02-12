# -*- coding: utf-8 -*-

import twitter


#コンシューマーキーやアクセストークンの情報を入力
	api = twitter.TwitterApi(	consumer_key		= 'your_consumer_key', 
		consumer_secret 		= 'your_consumer_secret', 
		access_token_key		= 'your_access_token_key', 
		access_token_secret	= 'your_access_token_secret', 
		input_encoding		= "UTF-8")

#twitterからフォローしてる人のリストを取得
friends = api.GetFriends()

f = open('job.txt', 'w')
for friend in friends:
	f.write(friend.screen_name + '\n')
f.close()