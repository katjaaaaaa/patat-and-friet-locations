# Patat and Friet locations
This repository is an addition to the research paper "The geographical difference in the usage of words "Patat" and "Friet" among Dutch speakers". Aside of necessary code we also provided this repository with output from the programs. In any command examples please change the standart s123456 to your own RUG number.  
Important note that the instructions below are mostly applied for users that use LWP remotely.

## Versions of the software
During the research the following versions of the software were used:
- Python 3.8.10  
- Ubuntu 20.04.4 LTS

## Instalment of the programs
All three programs are specified to work with Dutch Twitter data-set, provided by Rijksuniversiteit Groningen. To get access to all the data it is important to have access to LWP where data is located.  
To get acsess LWP use the following command and then insert RUG password ( If the terminal will ask for the fingerprint: type yes):  
```
ssh s4790383@karora.let.rug.nl
```
After logging in choose the directory where the programs will be located. This directory must have reading and writing permissions. The directory we used during the research is following:  
```
cd /home/s123456/Documents
```
Create the empty files and paste the code from the programs there:  
```
nano file_opener.py
nano random_date_generator.py
nano data_preprocessing.py
```
We created the copies of the programs in LWP. After that we can run the code in LWP environment and will recieve all possible output files in the current directory.

## Running the code
To run the code please insert the following command:  
```
python3 data_processing.py
```
There is no need in running other two files, as they are already included as modules in `data_processing.py`. 

## Running time and software recommendations  
As was mentioned in the paper, Dutch Twitter corpus contains a large amount of tweets. This feature greatly affects the code processing time. Normally it takes around 25-30 minutes to fully process the code and get the desired output. However, remote LWP contains a "very useful" feature that automatically logs the user out if he was inactive for a short period of time (e.g. he did not write any commands in the terminal). Therefore, **we highly recommend to occasionally (~ every 10 minutes) click on any key to keep the terminal "awake" during the code processing**, otherwise LWP will disconect you from the server and you will need to log in again.

## Desired output
The output of the `data_preprocessing.py` must contain two files: `friet_locations.json` and `patat_locations.json`. These files will be available in the working directory.  

Each day of month in Dutch Twitter corpus is divided in 24 hours. As expected, the amount of tweets contained during the night will be less than the amount of tweets contained during the day. One of our code limitations is the program uses all 24 hours to generate the filename that sometimes may affect the final data set. To avoid the "cherry-picking" data collecting we decided to keep the night hours as well the rest. Noneless be aware that because of this problem the numbers of the final data set may differ from the results, collected during the research.

## Importing data from LWP to the PC
There might also be need to import the necessary data from LWP invironment back to the PC's directory. To achieve this please go in the terminal to the directory you want to transfer the files to and insert the following command:
```
 scp -r s123456@karora.let.rug.nl:/home/s123456/Documents/<file_name.format> .
```
