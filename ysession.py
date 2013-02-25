#Creating a session
from dropbox import client, rest, session

#App secrets
APP_KEY= 'km1c74y77761m5v'
APP_SECRET = 'vf4pt5c1pul060d'
ACCESS_TYPE = 'dropbox'

#getting access token from file
try:
	f=open('cred.yb')
except IOError:
	print 'Credential file not created. Please login.'
	exit()
	
access_token,access_token_secret = f.read().split('|')
f.close()

#create session
sess = session.DropboxSession(APP_KEY,APP_SECRET, ACCESS_TYPE )
sess.set_token(access_token,access_token_secret)
client = client.DropboxClient(sess)