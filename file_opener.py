# Name program: file_opener.py
# Author: Katja Kamyshanova
# Date: 29-03-2022
# This program extracts data from a zipped .out file, converts it into
# a .json file, then splits its elements and returns them in a list

import json
import os
import gzip
import shutil

def path_change(filename, dif_path):

	'''Takes filename and path as strings, adds 
	directories according to data from the file
	and returns new path as a string'''

	month = filename[4:6]
	year = filename[0:4]
	dif_path = dif_path + year + "/" + month
	
	return dif_path

def open_file(filename_list):

	'''This function takes a list of files, opens each
	file in .json format, reads it, extracts data and
	returns all collected data in a list'''

	cur_path = os.getcwd() # returns an absolute path to current directory
	dif_path = "/net/corpora/twitter2/Tweets/"
	data_list = []

	for filename in filename_list:

		changed_path = path_change(filename, dif_path)
		os.chdir(changed_path) # changing path to get access to Twitter data
		with gzip.open(filename, 'rb') as f_in:
			os.chdir(cur_path) # going back to current dir to create a file with collected data
			with open('twitter_data.json', 'wb') as f_out:
				shutil.copyfileobj(f_in, f_out)
		
		with open('twitter_data.json','r') as f:
			data = f.readlines()
			for i in data[:-1]:
				if i != "\n":
					data_list.append(json.loads(i))

	return data_list # returning a list of all tweets collected from files

