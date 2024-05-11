#Nolan Christensen 010524411
from classHashTable import HashTable
from CsvFileReader import readCsvFile
from classVertex import Vertex
from classGraph import Graph
from classPackage import Package
from classTruck import Truck

numOfPackages = 0

csvPackageTableData = readCsvFile('WGUPS Package File.csv') # Get package data as array of arrays: [['1', '195 W Oakland Ave', 'Salt Lake City', 'UT', '84115', '0.4375', '21', ''], ...]

packageDataHashTable = HashTable() 
for row in csvPackageTableData:
        key = int(row[0])
        value = Package(row[1], row[2], row[3], row[4], row[5], row[6], row[7]) # Insert package object into the value portion of the key value pair
        packageDataHashTable.insert(key, value) #package data ex: (1, [package.address, package.city...TODO:, 'UT', '84115', '0.4375', '21', ''])
        numOfPackages += 1

#packageDataHashTable.displayHashTableData(numOfPackages)

csvDistanceTableData = readCsvFile('WGUPS Distance Table.csv') #Import the data from WGUPS distance file

# This for loop will fill in the diagonal mirror image data in the csvDistanceTableData list.
# This will make it possible create a vertex edgesList for each row in the list.
for i, row in enumerate(csvDistanceTableData):
    for j, col in enumerate(row):
        if col == '' and csvDistanceTableData[i][j] != 0 and i > 1 and j > 2:
            csvDistanceTableData[i][j] = csvDistanceTableData[j][i]
        #print(csvDistanceTableData[i][j])
        
#TODO: Get the data from the hashtable and use it to create vertices. Check that data was inserted correctly.
vertices = [] #List to store Vertex() objects

# Create the Vertices
for i, row in enumerate(csvDistanceTableData):
        if i > 1:
                newVertex = Vertex()
                newVertex.address = row[1]
                vertices.append(newVertex)
                #print(newVertex)

# Add vertices to each other's edgeLists with corresponding distance information.
for i, row in enumerate(csvDistanceTableData):
        if i > 1: #i > 1: Skip the first two rows in imported CSV fileData.
                for j, col in enumerate(row):
                        if csvDistanceTableData[i][j] != 0 and j > 2: # j > 2: Skip the first three columns in imported CSV fileData.
                                for curr_vertex in vertices:
                                        if curr_vertex.address == csvDistanceTableData[1][j]: # iterate through vertices list, find vertex() object with vertex.address equal to the current column address. Use that object to create new edge
                                                vertices[i-2].AddEdge(curr_vertex, float(csvDistanceTableData[i][j]))
                                                print(vertices[i-2])
                                                break

g = Graph()

# []
#print(g)

#TODO: We need a function in the that can take an address and 
# return a package id for the start vertex and the end vertex

#TODO: We need an Adjacency Matrix!!!!

# TODO: The Graph still needs undirected edges between vertices.
#dijkstra_shortest_path(g, )
# add Edges 
#g.add_undirected_edge(vertex_1, vertex_2, 484) # 484 miles
#g.add_undirected_edge(vertex_1, vertex_3, 626)
#g.add_undirected_edge(vertex_2, vertex_6, 1306)
#g.add_undirected_edge(vertex_3, vertex_5, 774)
#g.add_undirected_edge(vertex_3, vertex_4, 687)
#g.add_undirected_edge(vertex_4, vertex_11, 797)
#g.add_undirected_edge(vertex_5, vertex_6, 482)
#g.add_undirected_edge(vertex_6, vertex_7, 936)
#g.add_undirected_edge(vertex_7, vertex_8, 535)
#g.add_undirected_edge(vertex_7, vertex_9, 504)
#g.add_undirected_edge(vertex_9, vertex_10, 594)
#g.add_undirected_edge(vertex_11, vertex_5, 970)
#g.add_undirected_edge(vertex_11, vertex_8, 664)
#g.add_undirected_edge(vertex_11, vertex_9, 567)
#g.add_undirected_edge(vertex_11, vertex_10, 453)
 
#TODO: Use dijkstra's algorithm as a model to create an algorithm that can find 
# the shortest path for each truck from vertex to vertex until all the stops (vertices) have been visited.
# 

#TODO: Once two seperate instances (two trucks) of the shortest paths are determined, 
# use the rate at which they drive (18mph) to determine when they get to each vertex.