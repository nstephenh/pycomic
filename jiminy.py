#zip-a-de do-dah
#Its a pun
#jiminiy zips comics and spits out .cbz files with the date.

import datetime
import zipfile
import os
def makecbz(comicname , downloaddir):
	outputcbz = zipfile.ZipFile(downloaddir + "/" + comicname +".cbz", 'w')
	comicdir = downloaddir + "/" + comicname + "/"
	pagelist = os.listdir(comicdir)
	try:
		pagelist.sort()
	except Exception as e:
		print(e)
	for page in pagelist:
		outputcbz.write(comicdir + page)
	print("Sucessfully made .cbz for " + comicname)

