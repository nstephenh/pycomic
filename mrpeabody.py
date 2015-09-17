#Named after Mr Peabody from Peabody and Sherman
import os

def readdef(defdirectory):
	comiclist =[]
	try:
		os.mkdir(defdirectory)
	except:
		print("Definition Directory already exists")
	#Reads definition files from the file directory
	for deffilename in os.listdir(defdirectory):
		deffile = open(defdirectory +  "/" + deffilename, "r")
		defline = ""
		comicdef = []
		while True:
			#reads each line in the file, and writes it to comicdef until the last line is reached
			#except for the last two characters which are newline
			defline = deffile.readline()[:-1]
			print(defline)
			#Support for commented definition files
			if defline == "":
				break
			elif defline[0] != "#":
				comicdef.append(str(defline))
		#writes all but the last (blank) line of comcidef to the comiclist array
		comiclist.append(comicdef)
	return comiclist
