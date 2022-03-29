# Name program: data_preprocessing.py
# Author: Katja Kamyshanova
# Date: 28-03-2022
# This program takes a list of random generated files from Twitter data corpus, processes
# them in .json format, extracts the tweets that contain "friet" or "patat" in "text" value
# and available "place" value and returns the locations of these tweets "patat/friet" divided

import file_opener
import random_date_generator
import json
import os

def main():

    startyear = 2011
    endyear = 2022 # this year is not included in dates generator

    preprocess_data_friet = ['friet', 'frieten', 'frietjes','Friet', 'Frieten','Frietjes']
    preprocess_data_patat = ['patat','patatjes','Patat','Patatjes']

    # module returns a list of 11 lists with 13 random generated files per each list
    random_files_list = random_date_generator.dates_generator(startyear,endyear)

    friet_locations_list = []
    patat_locations_list = []
    tweets_total = 0

    for year in random_files_list:
        # module returns a a list of all tweets from 13 files in .json format
        year_data_list = file_opener.open_file(year)
        tweets_total += len(year_data_list)

        for day_data_list in year_data_list:
            encounter_f = 0
            encounter_p = 0

            for key,value in day_data_list.items():
                if key == "text":
                   if "RT" not in value and any(word in value for word in preprocess_data_friet):
                       encounter_f += 1
                   elif "RT" not in value and any(word in value for word in preprocess_data_patat):
                       encounter_p += 1
                if key == "place" and encounter_f != 0:
                    if value != None:
                        friet_locations_list.append(value)
                elif key == "place" and encounter_p != 0:
                    if value != None:
                       patat_locations_list.append(value)
            
        startyear += 1
    
    with open("friet_locations.json","w") as f:
        json.dump(friet_locations_list,f, indent=2)

    with open("patat_locations.json","w") as f1:
        json.dump(patat_locations_list,f1, indent=2)

    sum_tweets = len(friet_locations_list) + len(patat_locations_list)

    print("The total amount of collected tweets: " + str(tweets_total))
    print("The total amount of sorted tweets: " + str(sum_tweets))
    print("The amount of tweets falling under 'patat' category: " + str(len(patat_locations_list)))
    print("The amount of tweets falling under 'friet' category: " + str(len(friet_locations_list)))

if __name__ == "__main__":
    main()
