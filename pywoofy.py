print("Pywoofy")

import fetcher
import cracker
keeprunning = 1
# comic name, starturl, nextlinkregex, imgregex
comiclist=[["grrl power", """http://grrlpowercomic.com/archives/48""","""<a href="(.*)" class="navi navi-next" title="Next">Next</a>""","""<img srce"(.*)" alt=".*" title=".*" class="ishadow40" />"""]]

download_directory = "../comics/"

while keeprunning == 1:
	for comicdef in comiclist:
		fetcher.fetchcomic(comicdef,download_directory)
	keeprunning = 0
