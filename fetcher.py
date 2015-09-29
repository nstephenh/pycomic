#Downloads the html available on the specified page
import urllib.request

import time

import cracker
import mrpeabody

notarobotheader = {'User-Agent': 'Mozilla/5.0'}

def fetchpage(url):
	req = urllib.request.Request(url, headers=notarobotheader)
	try:
		print("downloading page " + url)
		return str(urllib.request.urlopen(req).read())
		

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
	#Sets the first page to be the start page
	current_page_url = comicdef[1]

	#As long as there is a next page to get, get that page
	while current_page_url != None:
		#get the current pages contents
		pagefeed = fetchpageretry(current_page_url)
		
		#find and download the image from said page
		img_url = cracker.findurl(pagefeed, comicdef[3], comicdef[4])
		if img_url == None:
			print("No image found")
			break
		print("downloading image " + img_url)

		downloadcomicdir = download_directory + "/" + comicdef[0] + "/"
		if comicdef[5] != "#useurlflag":
			downloadfilename = img_url.split("/")[-1]
		else:
			downloadfilename = current_page_url.split("/")[-1]
		
		#urllib.request.urlretrieve(img_url, downloadcomicdir + downloadfilename)

		filetosave = open(downloadcomicdir + downloadfilename, "wb")
		
		filetosave.write(urllib.request.urlopen(urllib.request.Request(img_url, headers=notarobotheader)).read())
		filetosave.close()
	
		#fetch the next page
		current_page_url = cracker.findurl(pagefeed, comicdef[2], comicdef[4])
		#update the database to reflect the next page
		comicdef[1] = current_page_url
		mrpeabody.updatedb(comicdef, download_directory)
	print("Finished downloading " + comicdef[0])
	return current_page_url

