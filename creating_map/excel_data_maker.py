# Name program: excel_data_maker.py
# Author: Katja Kamyshanova
# Date: 29-03-2022
# This program extracts from 2 .json files locations of the tweets,
# creates from them "friet-location" and "patat-location" excel files

import json
import pandas as pd

def nl_change(l):
    # Corrects the name of the country to standart "The Netherlands"
    changed_l = []
    for i in l:
        changed_l.append(i.split(","))

    for i in changed_l:
        if len(i) == 1:
            i.append("The Netherlands")
        else:
            i[1] = "The Netherlands"

    return changed_l

def be_change(l):
    # Corrects the name of the country to standart "Belgium"
    changed_l = []
    for i in l:
        changed_l.append(i.split(","))

    for i in changed_l:
        if len(i) == 1:
            i.append("Belgium")
        else:
            i[1] = "Belgium"
        
    return changed_l



def main():

    nl_list_f = []
    be_list_f =[]

    nl_list_p = []
    be_list_p = []

    with open("friet_locations.json","r") as f:
        data_list_f = json.loads(f.read())

    with open("patat_locations.json", "r") as f1:
        data_list_p = json.loads(f1.read())

    for i in data_list_f: # Extracts locations from NL and BE only
        if i["country_code"] == "NL":
            nl_list_f.append(i["full_name"])
        elif i["country_code"] == "BE":
            be_list_f.append(i["full_name"])


    for i in data_list_p:
        if i["country_code"] == "NL":
            nl_list_p.append(i["full_name"])
        elif i["country_code"] == "BE":
            be_list_p.append(i["full_name"])


    f_data = nl_change(nl_list_f) + be_change(be_list_f)
    p_data = nl_change(nl_list_p) + be_change(be_list_p)

    pd.DataFrame(f_data).to_excel('friet_data.xlsx', header=False, index=False) # converts a list into 
    pd.DataFrame(p_data).to_excel('patat_data.xlsx', header=False, index=False)

if __name__ == "__main__":
    main()