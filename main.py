#Nolan Christensen 010524411
from classHashTable import HashTable
from CsvFileReader import readCsvFile
from classVertex import Vertex
from classGraph import Graph
from classPackage import Package
from classTruck import Truck
from classAdjacencyMatrix import AdjacencyMatrix

csvAdjacencyMatrix_distanceData = readCsvFile('WGUPS Distance Table.csv') #Import the data from WGUPS distance file

#This for loop will fill in a diagonal mirror (creating a symmetric matrix, or adjacency matrix) for the data in the csvAdjacencyMatrix_distanceData list.
#This will make it possible create a vertex for each row in the csvAdjacencyMatrix_distanceData file.
for i, row in enumerate(csvAdjacencyMatrix_distanceData):
    for j, col in enumerate(row):
        if col == '' and csvAdjacencyMatrix_distanceData[i][j] != 0 and i > 1 and j > 2:
            csvAdjacencyMatrix_distanceData[i][j] = csvAdjacencyMatrix_distanceData[j][i]
            
AdjacencyMatrix.set_matrix(csvAdjacencyMatrix_distanceData)
        #print(csvAdjacencyMatrix_distanceData[i][j])
        
#vertices = [] #List to store Vertex() objects

#Create the Vertices and add their address property.
#for i, row in enumerate(csvAdjacencyMatrix_distanceData):
#        if i > 1:
#                newVertex = Vertex()
#                newVertex.address = row[1]
#                vertices.append(newVertex)
                #print(newVertex)

#Add vertices to each other's edgeLists with corresponding distance information.
#for i, row in enumerate(csvAdjacencyMatrix_distanceData):
#        if i > 1: #i > 1: Skip the first two rows in imported CSV fileData.
#                for j, col in enumerate(row):
#                        if csvAdjacencyMatrix_distanceData[i][j] != 0 and j > 2: #j > 2: Skip the first three columns in imported CSV fileData.
#                                for curr_vertex in vertices:
#                                        if curr_vertex.address == csvAdjacencyMatrix_distanceData[1][j]: #iterate through vertices list, find vertex() object with vertex.address equal to the current column address. Use that object to create new edge
#                                                vertices[i-2].AddEdge(curr_vertex, float(csvAdjacencyMatrix_distanceData[i][j]))
#                                                #print(vertices[i-2])
#                                                break

#Get package data as array of arrays: [['1', '195 W Oakland Ave', 'Salt Lake City', 'UT', '84115', '0.4375', '21', ''], ...]
csvTable_packageData = readCsvFile('WGUPS Package File.csv') 

hashTable_packageData = HashTable()

for row in csvTable_packageData:
        key = int(row[0])
        #vertexObj = Vertex() #Add a the vertex with the matching address to the package class object.
        
        #for current_vertex in vertices: 
        #        if row[1] == current_vertex.address:
        #                vertexObj = current_vertex
        #                vertexObj.packageId = row[0] #Add the packageId to the vertex object so they can relate to eachother easily.
        #                break
                        
        value = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])#, vertexObj) #Insert package object into the value portion of the key value pair
        hashTable_packageData.insert(key, value) #package data ex: (1, [package.address, package.city...TODO:, 'UT', '84115', '0.4375', '21', ''])

#hashTable_packageData.displayHashTableData()

#Setting up the graph with vertices that the trucks will use later to route their path.
#graph = Graph(csvAdjacencyMatrix_distanceData)
#graph.AddVertexList(vertices)

#for i, row in enumerate(csvAdjacencyMatrix_distanceData):
#        if i > 1: #i > 1: Skip the first two rows in imported CSV fileData.
#                for j, col in enumerate(row):
#                        if csvAdjacencyMatrix_distanceData[i][j] != 0 and j > 2: #j > 2: Skip the first three columns in imported CSV fileData.
#                                for curr_vertex in vertices:
#                                        if curr_vertex.address == csvAdjacencyMatrix_distanceData[1][j]: #iterate through vertices list, find vertex() object with vertex.address equal to the current column address. Use that object to create new edge
#                                                graph.AddUndirectedEdge(curr_vertex, float(csvAdjacencyMatrix_distanceData[i][j]))
#                                                break


        

#Initialize Truck objects to add packages to.
numTrucks = 3
truckFleetList = []
for i in range(1, numTrucks + 1):
    truckFleetList.append(Truck(i))

#truck1 packages: 4 19	20 21	28	40	14	15	16	25	26	34	11	23	6	12	17	31	32	22
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(4))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(19))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(20))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(21))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(28))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(40))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(14))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(15))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(16))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(25))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(26))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(34))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(11))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(23))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(6))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(12))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(17))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(31))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(32))
truckFleetList[0].AddPackage(hashTable_packageData.lookUp(22))

#truck2 packages: 1 3	8	9	30	13	27	35	39	10	2	7	29	33	24	5	37	38	4	36	18
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(1))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(3))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(8))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(9))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(30))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(13))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(27))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(35))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(39))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(10))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(2))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(7))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(29))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(33))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(24))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(5))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(37))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(38))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(36))
truckFleetList[1].AddPackage(hashTable_packageData.lookUp(18))

#TODO: Add packages to truck 3?
truckFleetList[0].DeliverPackages(csvAdjacencyMatrix_distanceData)
truckFleetList[1].DeliverPackages(csvAdjacencyMatrix_distanceData)

#graph.FindRoute(truck1.packageList)
#truck1Graph = Graph()
#for packages in truck1.packageList:
#        truck1Graph.AddVertex(packages.vertex)
##truck1Graph.NearestNeighborAlgorithm()
#
#truck2Graph = Graph()
#for packages in truck2.packageList:
#        truck2Graph.AddVertex(packages.vertex)
#        
#truck3Graph = Graph()
#for packages in truck3.packageList:
#        truck3Graph.AddVertex(packages.vertex)

# graph takes 2 addresses and loops over the packages 


#TODO: Once two seperate instances (two trucks) of the shortest paths are determined, 
# use the rate at which they drive (18mph) to determine when they get to each vertex.