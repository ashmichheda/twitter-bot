import tweepy

print("This is my twitter Bot!!!")

CONSUMER_KEY = 'XtWIUZED3Zr4cekxfOXmq8RIS'
CONSUMER_SECRET = 'tZdufwyOepQCouCP0QyByk3yQyWSassyIUZXxbjW2XLYsWceeD'
ACCESS_KEY = '1104736880862486528-0U2LSjRt7WUmD45bCl2sdlf6PZaDbl'
ACCESS_SECRET = 'rPgr5NhQZLQRU5AeJoZTNa7LOgIdZbGAnGL4VDonqEQDf'

# setting up auth object

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# use this below 'api' object to read and write data to twitter
api = tweepy.API(auth)


mentions = api.mentions_timeline()

# mentions is like a list
for mention in mentions:

	print(str(mention.id) + " - " + mention.text)
	
	if '#helloworld' in mention.text.lower():
		print('Found #helloworld!')
		print('responding back ...')







