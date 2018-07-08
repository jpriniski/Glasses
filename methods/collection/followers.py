"""
Project: Glasses
File: followers.py
Description: methods for collecting and saving Twitter follower data. 
Authors: J. Hunter Priniski & Zach Horne
"""


import os
from TwitterAPI import TwitterPager

def get_followers(screen_names, connection, pager = True):

	follower_dict = {}
	
	for screen_name in screen_names:

		if pager is False:
			followers = connection.request('followers/ids', {'screen_name':screen_name})
			follower_dict[screen_name] = followers

		else:
			followers = []
			r = TwitterPager(connection, 'followers/ids', {'screen_name':screen_name})
			
			for item in r.get_iterator():
				followers.append(item)
			follower_dict[screen_name] = followers

	return follower_dict


def write_followers(screen_names):

	os.makedirs('followers', exist_ok=True)

	for screen_name, values in screen_names.items():

		filename = 'followers/' + screen_name + '_followers.txt'

		file = open(filename, 'w')
		for item in screen_names[screen_name]:
		  file.write("%s\n" % item)

	return
