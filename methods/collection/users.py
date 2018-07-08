"""
Project: Glasses
File: users.py
Description: methods for collecting and saving Twitter user data. 
Authors: J. Hunter Priniski & Zach Horne
"""

from TwitterAPI import TwitterAPI
import re
import urllib.request
import json
from random import randint
import time


def read_id_list(directory):
	users = []
	with open(directory,'r') as file: 
		for line in file:
			#stripped = line[:-2]
			#if len(stripped) > 0:
			users.append(str(re.sub('\D','',line)))

	return users

def pop(list, start = 0, end = 100):
	#Python's native pop doesn't have functionality we need. 
	popped = list[start:end]
	new_list = [x for x in list if x not in popped]
	return popped, new_list

def get_run_time(leng):
	if leng < 900:
		return 0
	else:
		return (leng/900)*15

def stall(i):
	#Since we can run 9 iterations/calls to the API in a 15 min window
	#We need to keep track of how many calls we've made. 

	if i == 9:
		time.sleep(15*60)
		print("Long sleep")
		return 1 
	else:
		x = randint(0,20)
		time.sleep(x)
		print("Quick %d sec sleep" % x)
		return i + 1
	

def get_user_data(dir_to_id_list, connection, dir_ = 'user_data.txt'):

	id_list = read_id_list(dir_to_id_list)

	users_data = []
	i = 1

	while len(id_list) > 0:
		if len(id_list) > 100:
			print("%d min. remaining" % get_run_time(len(id_list)))
			id_search, id_list = pop(id_list, start = 0, end = 100)
		else:
			id_search, id_list = pop(id_list, start = 0, end = len(id_list))
			
		id_search = ','.join(id_search)
		request_ = connection.request('users/lookup', {'user_id':id_search})
		data = request_.json()



		#this needs to be changed, we can't dump json objects to a file, the items in the file need to be speerately inputed.  
		with open(dir_, 'a') as f:
			json.dump(data, f)
		print('Wrote users to data file')
		
		i = stall(i)
		

	return users_data
