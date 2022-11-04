# json-file-Hashing-automation

Creating a programme to generate a json file and a sha256 and output.csv

#required
--import csv
--import json
--import hashlib
--from csv import writer
--from csv import reader

#script lang = python

How it works::
it runs on the terminal
-returns a prompt asking the user for the file path for the .CSV file
!!!example of how the file path might look : ./New_output/nft.CSV
ones the user inputs the path it returns
            a new .CSV file with new rows containing the hashed key of the specific json file for that row
            json files of each rows
***WHAT THE SCRIPT DOES
-it creates a json file for every line in the .csv file and stores them
-it hashes the json file of every line and appends the value beside the line in a new .csv file