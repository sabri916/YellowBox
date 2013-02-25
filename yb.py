import pickle
from dropbox import client, rest, session

APP_KEY= 'km1c74y77761m5v'
APP_SECRET = 'vf4pt5c1pul060d'
ACCESS_TYPE = 'dropbox'

sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
request_token = sess.obtain_request_token()
url = sess.build_authorize_url(request_token)
print "url:", url
print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
raw_input()
access_token = sess.obtain_access_token(request_token)

f=open('cred.yb','w+')
f.write("%s|%s"%(access_token.key,access_token.secret))

client = client.DropboxClient(sess)
print "linked account:", client.account_info()