print("Pywoofy")

import fetcher
import cracker
import mrpeabody

import sys
import threading


#Reads comic definitions from definition files in def directory
download_directory = "../comics"
comiclist = mrpeabody.initdb(download_directory)

mrpeabody.initdir(comiclist, download_directory)


for comicdef in comiclist:
	#Download the current comic
	thread = threading.Thread(target = fetcher.fetchcomic,args= (comicdef, download_directory), name= comicdef[0] )
	thread.start()

while threading.active_count() > 0:
	pass
print("Finished downloading all pages of all comics")

