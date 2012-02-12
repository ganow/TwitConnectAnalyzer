# -*- coding: utf-8 -*-

import twitter

f = open('job.txt', 'r')
lines = f.read()
f.close()
job = lines.split('\n')

print '残りのユーザーは%d人です' % (len(job))
print job

checker = 0
i = 0

reslut = open('result.txt', 'a')
for i in range(len(job)):
	if job[i] != 'NOBODY':
		api = twitter.TwitterApi(	consumer_key		= 'your_consumer_key', 
			consumer_secret 		= 'your_consumer_secret', 
			access_token_key		= 'your_access_token_key', 
			access_token_secret	= 'your_access_token_secret', 
			input_encoding		= "UTF-8")

		#twitterからフォローしてる人のリストを取得
		friends = api.GetFriends(job[i])
		checker += len(friends)/100

		#自分と自分がフォローしている人の間にエッジを張る
		myname = job[i]
		for friend in friends:
		    print myname + ' follows ' + friend.screen_name
		    reslut.write(myname + ',follows,' + friend.screen_name + '\n')
		job[i] = 'NOBODY'
		f = open('job.txt', 'w')
		for j in len(job):
			if j <= i:
				f.write('NOBODY\n')
			else:
				f.write(job[j] + '\n')
		f.close()

		if checker >= 300:
			print 'API上限です\n'
			break
reslut.close()

print '終了しました。'
