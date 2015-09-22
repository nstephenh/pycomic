print("Pywoofy")

import fetcher
import cracker
import mrpeabody

import os

keeprunning = 1

#Reads comic definitions from definition files in def directory
download_directory = "../comics"
comiclist = mrpeabody.initdb("../comics")

mrpeabody.initdir(comiclist, download_directory)

#Interpret Call arguments


while keeprunning == 1:
	for comicdef in comiclist:
		#Download the current comic
		fetcher.fetchcomic(comicdef,download_directory)
	
	keeprunning = 0
