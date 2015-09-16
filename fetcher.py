#Downloads the html available on the specified page
import urllib.request

import time

import cracker


def fetchpage(url):
	try:
		print("downloading page " + url)
		return str(urllib.request.urlopen(url).read())
		
		#The following is for testing purposes only
		#return """<a href="content/nextpage/example.test" class="navi navi-next" title="Next">Next</a>"""

	except urllib.error.URLError as e:
		print(e)
		return None
def fetchpageretry(url):
	for i in range (10):
		pagefeed = fetchpage(url)
		if pagefeed != None:
			return pagefeed
		else:
			print("Download failed on try %d, retrying" % i)
			time.sleep((i))
	return None 
def fetchcomic(comicdef, download_directory):
	""" 
	Precondition: 	comicdef is a list containing [name, startpage, nextregex, imgregex] 
			download_directory is a string 	
	"""
	current_page_url = comicdef[1]
	while current_page_url != "done":
		#get the current page
		pagefeed = fetchpageretry(current_page_url)
		if pagefeed == None:
			current_page_url = "done"
			print("Either internet is down or the last page of the comic was reached")
			break	
		#find and download the image to download_directory/comicname/the image's name
		img_url = cracker.findreplacespace(pagefeed, comicdef[3])
		print("downloading image " + img_url)
		print(urllib.request.urlretrieve(img_url, download_directory + comicdef[0] + img_url.split("/")[-1]))

		
		
		#fetch the next page
		current_page_url = cracker.findelement(pagefeed, comicdef[2])
		if current_page_url == "No internet connection" or current_page_url == None:
			current_page_url = "done"
			#this will stop the loop
	
