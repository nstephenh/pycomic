print("Pywoofy")

keeprunning = 1
# comic name, starturl, nextlinkregex, imgregex
comiclist=[["grrl power", """http://grrlpowercomic.com/archives/48", "<a href="(?<content>[^"]*?)" class="navi navi-next" title="Next">Next</a>""","""<img src="(?<content>[^"]*?)" alt="[^"]*?" title="[^"]*?" class="ishadow40" />"""]]

while keeprunning == 1:
	for comic in comiclist:
		print(comic[0])
	keeprunning = 0
