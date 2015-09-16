print("Pywoofy")

import fetcher
import cracker
keeprunning = 1
# comic name, starturl, nextlinkregex, imgregex
comiclist=[["grrl power", """http://grrlpowercomic.com/archives/48""","""<a href="(http://grrlpowercomic.com/archives/[^"]*?)" class="navi navi-next" title="Next">Next</a>""","""<img src="(http://grrlpowercomic.com/comics/[^"]*?)" alt="[^"]*?" title="[^"]*?" class="ishadow40" />"""]]

download_directory = "../comics"

while keeprunning == 1:
	for comicdef in comiclist:
		fetcher.fetchcomic(comicdef,download_directory)
	keeprunning = 0
