print("Pywoofy")

import fetcher
import cracker
keeprunning = 1
# comic name, starturl, nextlinkregex, imgregex
comiclist=[["grrl power", """http://grrlpowercomic.com/archives/48""","""<a href="(.*)" class="navi navi-next" title="Next">Next</a>""","""<img srce"(?<content>[^"]*?)" alt="[^"]*?" title="[^"]*?" class="ishadow40" \\\/>"""]]

while keeprunning == 1:
	for comicdef in comiclist:
		pagefeed = fetcher.fetchpage(comicdef[1])
		print(cracker.findelement(pagefeed, comicdef[2]))
	keeprunning = 0
