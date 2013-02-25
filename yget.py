#Uploads a file
#Syntax

## yget filenameToDownload
## yget destinationDirectory filenameToDownload

import ysession,sys
from dropbox import client, rest, session

PATH='/'
FILE=1
#Arrange arguments
if len(sys.argv)!=2:
	print 'Invalid arguments'
	exit()

try:
	f, metadata = ysession.client.get_file_and_metadata(sys.argv[FILE])
except dropbox.rest.ErrorResponse:
	print 'File does not exist or something. Try again!'
	exit()

out = open(sys.argv[FILE], 'w')
out.write(f.read())
out.close()