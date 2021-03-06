# pycomic

A webcomic downloader written in Python 3.

Requirements:

Python 3

Feel free to add a webcomic in the issue tracker.

##How to use:

  Download or clone the repository to wherever you want to store the comics
  
  Delete the definition files for comics you do not want, or follow directions to create your own definition file.
  
  Run pycomic.py
  
  pycomic.py will create a directory in the same directory as the pywoofy folder. It will contain a hidden database file in the download folder for each comic.
  
##Creating a definiton file:

  All definition files have the folling elements:
  
    comicname : The name of the comic
    
    starturl : The first page of the comic
    
    nextregex : a regular expression dictating the next button in the comic and capturing the next page
    
    imageregex : a regular expression dictating the image element and capturing the source
    
  Additionally, some comics have:
  
    rootcomicdir : this specifies the directory that image files are saved at if its not in the url specified by imageregex
    
  Each of these elements requires the name followed by a single space and then the element in question. The one exception is useurlflag, which is only required to be present and can be followed by anything.
  
  These definiton files support comments. Any line that starts with # wil not be processed.
  
  Here is an example definition file:
  
    comicname El Goonish Shive
    
    starturl http://www.egscomics.com/?date=2002-01-21
    
    nextregex <a href="([^"]*?)" class="next" rel="next">
    
    imageregex <img title="[^"]*?" src="([^"]*?)" id="comic" border="0" />
    
    rootcomicdir http://www.egscomics.com/
    
  Notice how useurlflag is not included, as it is not necessary.
  
