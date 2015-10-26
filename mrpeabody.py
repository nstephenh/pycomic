#Named after Mr Peabody from Peabody and Sherman
import os
import sqlite3

deflist = ["comicname" ,"starturl", "nextregex", "imageregex", "rootcomicdir", "useurlflag", "autonumber" ]

def initdef(defdirectory):
	comiclist =[]
	try:
		os.mkdir(defdirectory)
	except:
		print("Definition Directory already exists")
	#Reads definition files from the file directory
	for deffilename in os.listdir(defdirectory):
		if deffilename.split(".")[-1] == "def":
			comiclist.append(readdef(defdirectory + "/" + deffilename))
	return comiclist
def readdef(deffilepath):
	deffile = open(deffilepath, "r")
	defline = ""
	#list of the different things in a definition file

	#create and populate comicdef with placeholder values
	comicdef = {}
	for item in deflist:
			comicdef[item] = "#" + item
	while True:
		#reads each line in the file, and writes it to comicdef 
		#until the last line is reached
		#except for the last two characters which are newline
		defline = deffile.readline()[:-1]
		#Process the definition file
		if defline == "":
			break
		else:
			for item in deflist:
				if defline[ : len(item)] == item:
					comicdef[item] = defline[len(item)+1 : ]
	return comicdef		
		
def initdb(downloaddir, arg1, arg2):
	'''
	Precondition: download directory is a directory that exists
	This function will create a json database file and populate it with information 
		from the .def files in the def directory
	Returns: a list of all comics
	'''
	try:
		os.mkdir(downloaddir)
	except:
		print("Download Directory already exists")
	initdb = initdef("./def")
	comiclist = []
	for comicdef in initdb:
		print(comicdef["comicname"])
		filepath = downloaddir + "/" + comicdef["comicname"] + "/." + "".join(comicdef["comicname"].split())
		try:
			os.mkdir(downloaddir + "/" + comicdef["comicname"])
		except: 
			print("Directory already exists for " + comicdef["comicname"])
		try:
			# if the database file already exists, 
			open(filepath, "x")
			print("Database file for " + comicdef["comicname"] + " does not exist, creating database")
			conn = sqlite3.connect(filepath)
			db = conn.cursor()
			db.execute("CREATE TABLE comicdef (" + (" text, ".join(deflist) + " text")+ ")") 
			exportlist = []
			for i in deflist:
				exportlist.append(comicdef[i])
			db.execute("INSERT INTO  comicdef values (?,?,?,?,?,?,?)", exportlist) #INSERT THE VALUES
			conn.commit()
			conn.close()
		except Exception as e:
			#print(e)
			pass
		comiclist.append(comicdef["comicname"])
	return comiclist
	
def updatedb(item, value,  comic, downloaddir):
	filepath = downloaddir + "/" + comic + "/." + "".join(comic.split())
	conn = sqlite3.connect(filepath)
	db = conn.cursor()
	db.execute("update comicdef SET " +item + "=?", (value,))
	conn.commit()
	conn.close()
def readdb(comic, downloaddir):
	'''Reads the database and returns the definition as a list
	'''
	#reads a specific comic database, and returns the definition from that database
	filepath = downloaddir + "/" + comic + "/." + "".join(comic.split())
	conn = sqlite3.connect(filepath)#use filepath here!!!
	db = conn.cursor()
	db.execute("SELECT * FROM comicdef")
	importlist = db.fetchall()[0]
	comicdef = {}
	index = 0
	for i in deflist:
		comicdef[i] = importlist[index]
		index +=1
	return comicdef
