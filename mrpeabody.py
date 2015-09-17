#Named after Mr Peabody from Peabody and Sherman
import os

def readdef(defdirectory):
	comiclist =[]
	try:
		os.mkdir(defdirectory)
	except:
		print("Definition Directory already exists")
	#Reads definition files from the file directory
	for deffile in os.listdir(defdirectory):
		readline = None
		comicdef = []
		while readline != "":
			#reads each line in the file, and writes it to comicdef until the last line is reached"
			readline = deffile.readline()
			comicdef = comicdef.append(readline)
		#writes all but the last (blank) line of comcidef to the comiclist array
		comiclst.append(comicdef[:-1])
	return comiclist
		
		
	
