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
		
		#list of the different things in a definition file
		deflist = ["comicname" ,"starturl", "nextregex", "imageregex", "rootcomicdir" ]
		
		#create and populate comicdef with placeholder values
		comicdef = []
		for item in deflist:
			comicdef.append( "#" + item)
		while True:
			#reads each line in the file, and writes it to comicdef 
			#until the last line is reached
			#except for the last two characters which are newline
			defline = deffile.readline()[:-1]
			print(defline)
			
			#Process the definition file
			if defline == "":
				break
			else:
				for item in deflist:
					if defline[ : len(item)] == item:
						position = comicdef.index("#" + item)
						comicdef.remove("#" + item)
						comicdef.insert(position, defline[len(item)+1 : ])
			print(comicdef) 
		comiclist.append(comicdef)
	return comiclist

def initdir(comiclist, downloaddirectory):
	try:
		os.mkdir(downloaddirectory)
	except:
		print("Download Directory already exists")
	for comic in comiclist:
		try:
			os.mkdir(downloaddirectory + "/" + comic[0])
		except:
			print("Directory already exists for" + comic[0])

