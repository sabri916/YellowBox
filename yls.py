#yls

#list files

import ysession,sys
from dropbox import client, rest, session

if len(sys.argv)!=2:
	print 'Invalid Arguments'
	exit()

folder_metadata = ysession.client.metadata(sys.argv[1])

for i in folder_metadata['contents']:
	print i['path'].split('/')[-1]

