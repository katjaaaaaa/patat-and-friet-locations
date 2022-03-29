# Name program: random_date_generator.py
# Author: Katja Kamyshanova
# Date: 29-03-2022 
# This program generates 13 filenames for year year, checks if
# They exist in Twitter data setand returns them as a list of lists

# Functions random_date and str_time_prop were adapted from the code created by Tom Alsberg
# Link: https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates

import random
import time
import os
import errno

    
def str_time_prop(start_date, end_date, date_format, prop):

    '''This function takes startdate, enddate and time-format
    as strings, generates a random and returns it as a str'''

    # converting a str according to date format
    stime = time.mktime(time.strptime(start_date, date_format))
    etime = time.mktime(time.strptime(end_date, date_format))

    # using random module to generate a new date
    random_time = stime + prop * (etime - stime)

    # converting a new date according to date format
    return time.strftime(date_format, time.localtime(random_time))


def random_date(start, end, prop):

    # provides str_time_prop with a certian date format

    return str_time_prop(start, end, '%Y%m%d:%H', prop)


def dates_generator(startyear, endyear):

    '''This function takes two years as integers, generates
    13 lists with random filenames, checks if each file exists
    in dataset and returns these lists as one list '''

    cur_path = os.getcwd()
    dates_list = []
    dif_path = "/net/corpora/twitter2/Tweets/"
    while True:
        year_dates_list = []
        counter = 0
        while True:
            date = random_date(f"{str(startyear)}0101:00", f"{str(startyear)}1231:23", random.random()) + ".out.gz"
            month = date[4:6]
            changed_path = dif_path + str(startyear) + "/" + month
            os.chdir(changed_path) # navigating to the directory of a random file
            try:
                #with open(date) as f:
                if os.path.isfile(date): # checking if file exists in the directory
                    year_dates_list.append(date)
                    counter += 1
                if counter == 1: # generating 13 tweets per year
                    break
            except IOError as x: # skipping the file if there is no reading permission
                if x.errno == errno.EACCES: 
                    continue
            
        if len(year_dates_list) == len(set(year_dates_list)): # checking if any dublicates were created
            dates_list.append(year_dates_list) 
            startyear += 1
            if startyear == endyear:
                   break

    os.chdir(cur_path)

    return dates_list # returning all lists collected per year


