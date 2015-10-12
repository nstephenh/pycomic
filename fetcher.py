#Downloads the html available on the specified page
import urllib.request

import time

import cracker
import mrpeabody

notarobotheader = {'User-Agent': 'Mozilla/5.0'}

def fetchpage(url):
	req = urllib.request.Request(url, headers=notarobotheader)
	try:
		return str(urllib.request.urlopen(req).read())
		

	except urllib.error.URLError as e:
		print(e)
		return None
def fetchpageretry(url):
	for i in range (100):
		pagefeed = fetchpage(url)
		if pagefeed != None:
			return pagefeed
		else:
			print("Download of page" + url + " failed on try %d, retrying" % i)
			time.sleep((5*(i+1)))
	return None 

def fetchcomic(comic, download_directory):
	""" 
	Precondition: comic is the name of the comic, download_directory is a where all comics will be downloaded	
	"""

	#Read the database to get the definition
	comicdef = mrpeabody.readdb(comic, download_directory)	

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

		downloadcomicdir = download_directory + "/" + comicdef[0] + "/"
		if comicdef[5] != "#useurlflag":
			downloadfilename = current_page_url.split("/")[-1]
			try:
				downloadfilename = downloadfilename + "." +  img_url.split(".")[-1]
			except:
				pass
			try:
				downloadfilename = downloadfilename.split("=")[-1]
			except:
				pass
		else:
			downloadfilename = current_page_url.split("/")[-1]
		
		#urllib.request.urlretrieve(img_url, downloadcomicdir + downloadfilename)
		print("Downloading " + img_url + " as " + downloadfilename)
		filetosave = open(downloadcomicdir + downloadfilename, "wb")
		
		filetosave.write(urllib.request.urlopen(urllib.request.Request(img_url, headers=notarobotheader)).read())
		filetosave.close()
	
		
		#fetch the next page
		current_page_url = cracker.findurl(pagefeed, comicdef[2], comicdef[4])
		#update the database to reflect the next page
		if current_page_url != None:
			comicdef[1] = current_page_url
			mrpeabody.updatedb(comicdef, download_directory)
		
	print("Finished downloading " + comicdef[0])
	return current_page_url

