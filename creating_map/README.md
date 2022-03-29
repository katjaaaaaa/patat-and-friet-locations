# Creating a map from the results
To recreate the visual results that were used in the research we provided the `excel_data_maker.py` and instructions for installment and use of Microsoft PowerBI, the software for creating visualized data. The user is free to use any other software for creating the maps. The following steps apply for PowerBI (ver 2.103.881.0 64-bit) only.  

## Step 1: Preparing the data
After collecting the data, provided with `data_preprocessing.py` the user should receive two `.json` files, containing the necessary data:  
- `friet_locations.json`  
- `patat_locations.json`

This data is going to be used in extracting the necessary locations for future maps. To transfer the files from the LWP directory to the current directory please use in terminal the following command:  
```
scp -r s123456@karora.let.rug.nl:/home/s123456/Documents/friet_locations.json .  
scp -r s123456@karora.let.rug.nl:/home/s123456/Documents/patat_locations.json .  
```
-s number and path to the files must be changed to the users. After that, the terminal will ask the user for the RUG password and download the necessary data if the password is correct. The files will appear in the current directory. Please check if the files and the program are located in the same directory.   

## Step 2: Installing necessary modules
Before running the program please install two necessary packages:  
-`pip3 install pandas` a python library that provides a transfer to excel files  
-`pip3 install openpyxl` an addition for pandas 

## Step 4: Running the code and changing the format
After installing all necessary packages run the code with a command:  
```
python3 excel_data_maker.py
```
This directory will receive two excel files: `patat_data.xlsx` and `friet_data.xlsx`. However, to use these files in the software they must be changed into `.csv` format. Please provide the correct formats to these files via Microsoft Excel or other programs. 

## Step 3: Installing PowerBI (Dekstop)
Microsoft PowerBI is software that is used to visualize different formats of data. All the necessary features are free (for Windows users) and can be easily downloaded via Microsoft Store. We provided a [link](https://www.microsoft.com/en-us/download/details.aspx?id=58494) on downloading page of this software. Mac users might encounter difficulties with installing Microsoft products. Here is a [link](https://www.holistics.io/blog/how-to-use-power-bi-on-mac-devices/) with possible solutions for this problem.  
All further steps will apply to PowerBI. 

## Step 4: Creating maps
Open PowerBI to get started with map-creating. There is no need in creating a new file. To get data from  `patat_data.csv` and `friet_data.csv` please follow the commands:  
Home > Get Data > Text/CSV > Choose the directory where files are located > Choose the files > Load. Note that the files must be located in any directory of the user's PC to be imported (not in Ubuntu's directory) otherwise, PowerBI will give an "Unable to connect" error. Both files will be transferred to the right panel.  
Click on the file "friet_data" and set a mark on "Column 1". PowerBI will create a field on the workspace and show the row with different cities. To make from this row of data a map please follow the following commands  
Click on "Column1" > Column Tools > Data Category > City. After that an icon of "Column 1" will change. Click in "Column 1" and "drag" it to the left so the map will appear. Repeat the same steps for "patat_data".
