#zip-a-de do-dah
#Its a pun
#jiminiy zips comics and spits out .cbz files with the date.

import datetime
import ZipFile

def makecbz(comicname , downloaddir):
	timedatestamp = str(datetime.now())
	outputcbz = ZipFile.open(comicname + "_" +timedatestamp + ".cbz", 'x')
	for page in os.listdir(downloaddir + "/" + comicname):
		outputcbz.write(page)
	print("Sucessfully made .cbz for " + comicname)

