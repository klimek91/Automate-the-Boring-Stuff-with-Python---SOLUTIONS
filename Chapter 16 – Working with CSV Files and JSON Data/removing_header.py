import csv, os

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        csvFile = open(file)
        csvData = list(csv.reader(csvFile))
        newData = csvData[1:]

        outputFile = open(file.replace('.csv','_new.csv'),'w', newline='')
        outputWriter = csv.writer(outputFile)
        for row in newData:
            outputWriter.writerow(row)
        outputFile.close()
        csvFile.close()