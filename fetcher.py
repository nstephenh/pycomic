#Downloads the html available on the specified page
import urllib2
import cracker
def fetchpage(url):
	try:
		return urllib2.urlopen(url).read()
		#The following is for testing purposes only
		#return """<a href="content/nextpage/example.test" class="navi navi-next" title="Next">Next</a>"""

	except:
		print("No internet Connection")	
		return "No internet Connection"
def fetchcomic(comicdef, download_directory):
	""" 
	Precondition: comicdef is a list containing [name, startpage, nextregex, imgregex] 
	
	"""
	current_page_url = comicdef[1]
	while current_page_url != "done":
		#get the current page
		pagefeed = fetchpage(current_page_url)
		
		#find and download the image to download_directory/comicname/the image's name
		img_url = cracker.findelement(pagefeed, comicdef[3])
		print("downloading " + img_url)
		urllib2.urlretrieve(img_url, download_directory + comic_name + img_url.split("/")[-1])
		
		
		#fetch the next page
		current_page_url = cracker.findelement(pagefeed, comicdef[2])[1]
		if current_page_url == "No internet connection" or current_page_url == None:
			current_page_url = "done"
			#this will stop the loop
	
