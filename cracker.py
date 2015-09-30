#seeks out specific parts of the webpage
#name based off of cracker, a fictional dog detecting booby traps in vietnam
import re

def findelement(pagefeed, elementregex):
	regex = re.compile(elementregex)
	results =regex.search(pagefeed)
	if results != None:
		#returns if the item exists, replacing spaces with %20
		return str.replace(results.group(1), " ", "%20")
	else:
		#if the item does no exist, return None
		return None
def findurl(pagefeed, elementregex, siteurl):
	element = findelement(pagefeed, elementregex)
	#if the element isn't an absolute link, then make it one
	if element != None and element[:4] != "http":
		if siteurl == "#rootcomicdir":
			print ("Error, comic requires rootcomicdir and none specified")
		else:
			try:
				return (siteurl + element.split("./")[1])
			except IndexError: #If the url doesn't contain "./" then we don't need to include that
				return (siteurl + element)
				
	elif element != None:
		return element
	else:
		return None
