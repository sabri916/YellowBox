#Uploads a file
#Syntax

## yput filenameToUpload
## yput destinationDirectory filenameToUpload

import ysession,sys
from dropbox import client, rest, session

PATH='/'

#Arrange arguments
if len(sys.argv)==2:
	FILE=1
elif len(sys.argv)==3:
	FILE=2
	PATH=sys.argv[1]
else:
	print 'Invalid arguments'
	exit()

#open file
try:
	f = open(sys.argv[FILE])
except IOError:
	print 'File does not exist.'
	exit()
	
#upload and print response
response = ysession.client.put_file(PATH+'/'+sys.argv[FILE],f)
print 'uploaded: ',response