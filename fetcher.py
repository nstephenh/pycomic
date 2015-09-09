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
def fetchcomic(url):
	while url != "No internet Connection":
		#fetch the image here
		url = cracker.findelement(fetchpage(url))
			
