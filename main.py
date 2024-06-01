#Nolan Christensen 010524411
from classHashTable import HashTable
from CsvFileReader import readCsvFile
from classPackage import Package
from classTruck import Truck
from classAdjacencyMatrix import AdjacencyMatrix
from datetime import datetime, time
from funcMenu import menu

#Overall time Complexity: O(n^2)

#Time complexity: O(n), Import the data from WGUPS distance file
csvAdjacencyMatrix_distanceData = readCsvFile('WGUPS Distance Table.csv') 

#Time complexity: O(n^2) for each new address, This for loop will fill in a diagonal mirror 
#(creating a symmetric matrix, or adjacency matrix) for the data in the csvAdjacencyMatrix_distanceData list.
#This will make it possible create a vertex for each row in the csvAdjacencyMatrix_distanceData file.
for i, row in enumerate(csvAdjacencyMatrix_distanceData):
    for j, col in enumerate(row):
        if col == '' and csvAdjacencyMatrix_distanceData[i][j] != 0 and i > 1 and j > 2:
            csvAdjacencyMatrix_distanceData[i][j] = csvAdjacencyMatrix_distanceData[j][i]

#Create an instance of the static adjacency matrix class. Other classes and functions can have access to the same adjacency matrix.
AdjacencyMatrix.set_matrix(csvAdjacencyMatrix_distanceData)

#Time complexity: O(n), Get package data as lists within a list: [['1', '195 W Oakland Ave', 'Salt Lake City', 'UT', '84115', '0.4375', '21', ''], ...]
csvTable_packageData = readCsvFile('WGUPS Package File.csv') 

#New instance of a hashtable.
hashTable_packageData = HashTable()

#Time complexity: O(n), Insert data from 'WGUPS Package File.csv' into the hash table in the form of package objects.
for row in csvTable_packageData:
        key = int(row[0])
        value = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) #Insert package object into the value portion of the key value pair
        hashTable_packageData.insert(key, value) #key_value pair example: [1, [package.id, package.address, package.city, package.state, package.zip, package.deadline, package.specialNotes]]

#Initialize Truck objects with id's in a list for loading packages.
numTrucks = 3
truckFleetList = []
for i in range(1, numTrucks + 1):
    truckFleetList.append(Truck(i))

#Load truck 1 with packages
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(20)) #DD: 10:30AM, Must be delivered with 13, 15
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(1)) #DD: 10:30 AM
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(40)) #DD: 10:30AM
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(14)) #DD: 10:30AM, Must be delivered with 15, 19
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(15)) #DD: 9:00am
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(16)) #DD: 10:30AM, Must be delivered with 13, 19
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(29)) #DD: 10:30AM
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(34)) #DD: 10:30AM
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(30)) #DD: 10:30AM
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(13)) #DD: 10:30AM
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(37)) #DD: 10:30AM
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(31)) #DD: 10:30AM
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(19))

#Load truck 2 with packages
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(4))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(21))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(28)) #Delayed on flight---will not arrive to depot until 9:05 am
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(3)) #Can only be on truck 2
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(7))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(6)) #DD: 10:30AM, Delayed on flight---will not arrive to depot until 9:05 am
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(33))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(24))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(5))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(25)) #DD: 10:30am, Delayed on flight---will not arrive to depot until 9:05 am
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(32)) #Delayed on flight---will not arrive to depot until 9:05 am
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(38)) #Can only be on truck 2
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(36)) #Can only be on truck 2
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(18)) #Can only be on truck 2
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(22))

#Load truck 3 with packages
truckFleetList[2].AddPackage(hashTable_packageData.lookUp(9)) #Wrong address listed (won't know until 10:20am)
truckFleetList[2].AddPackage(hashTable_packageData.lookUp(11))
truckFleetList[2].AddPackage(hashTable_packageData.lookUp(23))
truckFleetList[2].AddPackage(hashTable_packageData.lookUp(12))
truckFleetList[2].AddPackage(hashTable_packageData.lookUp(17))
truckFleetList[2].AddPackage(hashTable_packageData.lookUp(27))
truckFleetList[2].AddPackage(hashTable_packageData.lookUp(35))
truckFleetList[2].AddPackage(hashTable_packageData.lookUp(39))
truckFleetList[2].AddPackage(hashTable_packageData.lookUp(10))
truckFleetList[2].AddPackage(hashTable_packageData.lookUp(8))
truckFleetList[2].AddPackage(hashTable_packageData.lookUp(26))
truckFleetList[2].AddPackage(hashTable_packageData.lookUp(2))

truckFleetList[0].DeliverPackages() #Time complexity: O(n^2), Deliver the Packages for truck 1

truckFleetList[1].startDateTime = datetime.combine(datetime.today(), time(9, 5)) #Start truck 2 at 9:05am
truckFleetList[1].DeliverPackages() #Deliver the Packages for truck 2

truckFleetList[2].startDateTime = datetime.combine(datetime.today(), time(10, 20)) #Start truck 3 at 10:20am
truckFleetList[2].DeliverPackages() #Deliver the Packages for truck 2

menu(truckFleetList, hashTable_packageData)