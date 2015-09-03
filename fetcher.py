import urllib2

def fetch(comicdef):
	# comic name, starturl, nextlinkregex, imgregex
	print(comicdef[0])
	print(comicdef[1])
	starturl = comicdef[1]
	print(urllib2.urlopen(starturl).read())

			
