import hashlib
import csv
import json
from csv import writer
from csv import reader


#get's the file paths
datapath =input("paste your file path here: ")
outpath = datapath[0:-4]

#loops through the entire .CSV file and rtrieve every data
container = {}
hashes=['HASH']
with open(datapath, encoding='utf-8') as doc:
    data = csv.DictReader(doc)
    for i in data:
        rows = i['Name']
        container[rows] = i
        #converts every row into a json file
        miniContainer = {}
        miniContainer[rows] = i 
        with open(rows+'.json', 'w',  encoding='utf-8') as minidoc:
            minidoc.write(json.dumps(miniContainer, indent=4))
            # hashes each file and stores the value in the variable "hashes"
            with open(rows+'.json',"rb") as f:
                bytes = f.read() # read entire file as bytes
                readable_hash = hashlib.sha256(bytes).hexdigest();
                hashes.append(readable_hash)

# creates a .json copy of the csv file
with open(outpath+'.json', 'w',  encoding='utf-8') as outDoc:
        outDoc.write(json.dumps(container, indent=4))

    
# Open the input_file in read mode and output_file in write mode, creates a new column and merges every row with its hashed value
y = 0
with open(datapath, 'r') as read_obj, \
        open(outpath+'.output'+'.csv', 'w', newline='') as write_obj:
 # Create a csv.reader object from the input file object
    csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
    csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
    for row in csv_reader:
                # Append the default text in the row / list
        row.append(hashes[y])
                # Add the updated row / list to the output file
        csv_writer.writerow(row)
        y += 1