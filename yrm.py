#yrm

#deletes a file

#yrm file

import ysession,sys
from dropbox import client, rest, session

#Check arguments
if len(sys.argv)!=2:
	print 'Invalid arguments'
	exit()

#delete file
try:
	response = ysession.client.file_delete(sys.argv[1])
except rest.ErrorResponse:
	print 'File does not exist'