print("Pywoofy")

import fetcher
keeprunning = 1
# comic name, starturl, nextlinkregex, imgregex
comiclist=[["grrl power", """http://grrlpowercomic.com/archives/48", "<a href="(?<content>[^"]*?)" class="navi navi-next" title="Next">Next</a>""","""<img src="(?<content>[^"]*?)" alt="[^"]*?" title="[^"]*?" class="ishadow40" />"""]]

while keeprunning == 1:
	for comicdef in comiclist:
		fetcher.fetch(comicdef)
	keeprunning = 0
