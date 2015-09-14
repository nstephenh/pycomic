#seeks out specific parts of the webpage
#name based off of cracker, a fictional dog detecting booby traps in vietnam
import re

def findelement(pagefeed, elementregex):
	regex = re.compile(elementregex)
	print("searching for "+ elementregex)
	return regex.search(pagefeed).group(1)


