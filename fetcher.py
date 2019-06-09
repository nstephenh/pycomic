#Downloads the html available on the specified page
import requests
import time

import cracker
import mrpeabody
import jiminy

notarobotheader = {'User-Agent': 'Mozilla/5.0'}

def fetchpage(url):
	try:
		return str(requests.Session().get(url, headers=notarobotheader).text)
		

	except Exception as e:
		print(e)
		return None
def fetchpageretry(url):
	""" URL is the url of the page to download
	This calls the fetchpage function up to 100 times, with an increasing wait between each time
"""
	for i in range (100):
		pagefeed = fetchpage(url)
		if pagefeed != None:
			return pagefeed
		else:
			print("Download of page " + url + " failed on try %d, retrying" % i)
			time.sleep((5*(i+1)))
	return None 

def fetchcomic(comic, download_directory):
	""" 
	Precondition: comic is the name of the comic, download_directory is a where all comics will be downloaded	
	"""

	#Read the database to get the definition
	comicdef = mrpeabody.readdb(comic, download_directory)
	#Sets the first page to be the start page
	current_page_url = comicdef["starturl"]
	if comicdef["autonumber"] != "#autonumber":
		autocount = int(comicdef["autonumber"])
	#As long as there is a next page to get, get that page
	while current_page_url != None:
		#get the current pages contents
		pagefeed = fetchpageretry(current_page_url)
		
		#find and download the image from said page
		img_url = cracker.findurl(pagefeed, comicdef["imageregex"], comicdef["rootcomicdir"])
		if img_url == None:
			print("No image found")
			break

		downloadcomicdir = download_directory + "/" + comicdef["comicname"] + "/"
		#if comicdef["autonumber"] != "#autonumber":
		downloadfilename = '0'*(8-len(str(autocount)))+ str(autocount) +"."+ img_url.split(".")[-1]
		#elif comicdef["useurlflag"] != "#useurlflag":
		#	downloadfilename = current_page_url.split("/")[-1]
		#	try:
		#		downloadfilename = downloadfilename + "." +  img_url.split(".")[-1]
		#	except:
		#		pass
		#	try:
		#		downloadfilename = downloadfilename.split("=")[-1]
		#	except:
		#		pass
		#else:
		#	downloadfilename = img_url.split("/")[-1]
		
		#urllib.request.urlretrieve(img_url, downloadcomicdir + downloadfilename)
		print("Downloading " + img_url + " as " + downloadfilename)
		filetosave = open(downloadcomicdir + downloadfilename, "wb")
		
		filetosave.write(requests.get(img_url, headers=notarobotheader).content)
		filetosave.close()
	
		
		#fetch the next page
		next_url = cracker.findurl(pagefeed, comicdef["nextregex"], comicdef["rootcomicdir"])
		if current_page_url == next_url:
		    current_page_url = None
		else:
		    current_page_url = next_url

		#update the database to reflect the next page
		if current_page_url != None:
			comicdef["starturl"] = current_page_url
			mrpeabody.updatedb("starturl", current_page_url, comic, download_directory)
			if comicdef["autonumber"] != "#autonumber":
				autocount +=1
				mrpeabody.updatedb("autonumber", autocount, comic, download_directory)
	print("Finished downloading " + comic)
	jiminy.makecbz(comic, download_directory)

