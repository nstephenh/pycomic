#seeks out specific parts of the webpage
#name based off of cracker, a fictional dog detecting booby traps in vietnam
import re

def findelement(pagefeed, elementregex):
	return re.split(elementregex, pagefeed)



