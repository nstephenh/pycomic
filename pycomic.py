print("Pywoofy")

import fetcher
import cracker
import mrpeabody

import sys
import threading
#Take in arguments
try:
	arg1 = sys.argv[1]
	arg2 = sys.argv[2]
except:
	arg1 = "None"
	arg2 = "None"

#Reads comic definitions from definition files in def directory
download_directory = "../comics"
comiclist = mrpeabody.initdb(download_directory, arg1, arg2)

for comic in comiclist:
	#Download the current comic
	thread = threading.Thread(target = fetcher.fetchcomic,args= (comic, download_directory), name = comic )
	thread.start()

#print("Finished downloading all pages of all comics")

