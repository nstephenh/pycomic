#zip-a-de do-dah
#Its a pun
#jiminiy zips comics and spits out .cbz files with the date.

import datetime
import zipfile
import os
def makecbz(comicname , downloaddir):
	timedatestamp = str(datetime.datetime.now()).split(".")[0]
	outputcbz = zipfile.ZipFile(downloaddir + "/" + comicname + " " +timedatestamp + ".cbz", 'w')
	comicdir = downloaddir + "/" + comicname + "/"
	for page in os.listdir(comicdir):
		outputcbz.write(comicdir + page)
	print("Sucessfully made .cbz for " + comicname)

