import csv, os

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        csvFile = open(file)
        csvData = list(csv.reader(csvFile))
        newData = csvData[1:]
