print("Pywoofy")

import fetcher
import cracker
import mrpeabody

import os

keeprunning = 1

#Reads comic definitions from definition files in def directory
comiclist = mrpeabody.readdef("./def")

download_directory = "../comics"
mrpeabody.initdir(comiclist, download_directory)

while keeprunning == 1:
	for comicdef in comiclist:
		fetcher.fetchcomic(comicdef,download_directory)
	keeprunning = 0
