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

FILE_NAME = 'last_seen_id.txt'


def retrieve_last_seen_id(file_name):
	f_read = open(file_name, 'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()
	return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return

# NOTE: Use 1145736989267771392 for testing
last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(last_seen_id, tweet_mode ='extended')

# mentions is like a list
for mention in mentions:

	print(str(mention.id) + " - " + mention.text)

	if '#helloworld' in mention.text.lower():
		print('Found #helloworld!')
		print('responding back ...')
