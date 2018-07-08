"""
Project: Glasses
File: images.py
Description: methods for collecting and saving Twitter profile images. 
Authors: J. Hunter Priniski & Zach Horne
"""

import urllib.request

#url <- the url address to the jpeg file (This is how Twitter stores profile images)
#file <- directory of where you want to save the image on your local machine
#NOTE: save_jpeg is optimized to work with Twitter jpeg URLS.  Therefore, setting high_res = False could lead to errors. 
def save_jpeg(url, file, high_res = True):

  #To get a higher resolution profile image, we will remove '_noraml' from the url if
  if high_res is True:
    url = url.replace('_normal','') 
	
  urllib.request.urlretrieve(url, file)

	return
