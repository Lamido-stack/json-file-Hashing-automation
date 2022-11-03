# import csv, json

# datapath = r"C:\Users\Lamido\Desktop\NFT Naming csv - All Teams.csv"
# outpath = r"C:\Users\Lamido\Desktop\nft\NFTinfo"

# data = {}
# with open(datapath) as csvFile:
#     csvReader = csv.DictReader(csvFile)
#     for rows in csvReader:
#         id = rows['SerialNumber']
#         data[id] = rows

# with open(outpath, 'w') as jsonFile:
#     jsonFile.write(json.dumps(data, indent=4))