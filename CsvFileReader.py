import csv

def readCsvFile(fileName):
    data = []
    with open(fileName, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data