import pandas as pd
import hashlib
from csv import writer
from csv import reader
#get's the file paths
datapath =input("paste your file path, NOTE: PANDA reqiu")
outpath = datapath[0:-4]

#reads through the csv file to be processed
data = pd.read_csv(datapath)



serialNum = data.SerialNumber
fileName = data.Filename
# description = data.Description
# gender = data.Gender
uuid = data.UUID

#container to store the contents of the csv file after
container ={}

x = 0

while x < len(fileName):
    container[fileName[x]]=[
        {"SerialNumber ":serialNum[x],
        "Filename ":fileName[x],
        "UUID ":uuid[x],}
        ]
    df = pd.DataFrame(container)
    df.to_json(outpath, indent=4)
    x = x+1

#converts every row into a json file, hashes each file 
hashes=['HASH']
for i in container:
    filePath = outpath+'.'+i+'.json'
    df = pd.DataFrame(container[i])
    df.to_json(filePath, indent=4)
    with open(filePath,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        hashes.append(readable_hash)
        
# Open the input_file in read mode and output_file in write mode, creates a new column and merges every row with its hashed value
y=0
while y < len(fileName):
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
