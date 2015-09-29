# pywoofy

A webcomic downloaded written in python.

Feel free to add a webcomic in the issue tracker

##How to use:

  Download or clone the repository to wherever you want to store the comics
  
  Delete the definition files for comics you do not want, or follow directions to create your own definition file.
  
  Run pywoofy.py
  
  Pywooy.py will create a directory in the same directory as the pywoofy folder. It will contain a hidden database file, and a folder for each comic
  
##Creating a definiton file:

  All definition files have the folling elements:
  
    comicname
    
    starturl
    
    nextregex
    
    imageregex
    
  Additionally, some comics have:
  
    rootcomicdir
    
    useurlflag
    
  Each of these elements requires the name followed by a single space and then the element in question. The one exception is useurlflag, which is only required to be present and can be followed by anything.
  
  These definiton files support comments. Any line that starts with # wil not be processed.
  
  Here is an example definition file:
  
    comicname El Goonish Shive
    
    starturl http://www.egscomics.com/?date=2002-01-21
    
    nextregex <a href="([^"]*?)" class="next" rel="next">
    
    imageregex <img title="[^"]*?" src="([^"]*?)" id="comic" border="0" />
    
    rootcomicdir http://www.egscomics.com/
    
  Notice how useurlflag is not included, as it is not necessary.
  
