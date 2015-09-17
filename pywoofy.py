print("Pywoofy")

import fetcher
import cracker
import mrpeabody

import os

keeprunning = 1

# comic name, starturl, nextlinkregex, imgregex
comiclist = mrpeabody.readdef("./def")

download_directory = "../comics"

while keeprunning == 1:
	for comicdef in comiclist:
		fetcher.fetchcomic(comicdef,download_directory)
	keeprunning = 0
