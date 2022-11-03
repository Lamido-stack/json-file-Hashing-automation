# json-file-Hashing-automation

Creating a programme to generate a json file and a sha256 and output.csv

#required
--import pandas as pd
--import hashlib
--from csv import writer
--from csv import reader

#script lang = python

How it works::
it runs on the terminal
the keyvalues or headers for every row has to follow a format(current format: "SerialNumber, filename, UUID")
-returns a prompt asking the user for the file path for the .CSV file
ones the user inputs the path it returns
            a new .CSV file with new rows containing the hashed key of the specific json file for that row
            json files of each rows
!!It can be modified to work with different csv file content as the need may be
