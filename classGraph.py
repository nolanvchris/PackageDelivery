
from classVertex import Vertex
from classPackage import Package

class Graph:
    def __init__(self, p_adjacencyMatrix):
        self.adjacencyMatrix = p_adjacencyMatrix
        #self.vertexList = []
        #self.edgeWeights = []
        
    def __str__(self):
        return "%s\n" % (self.adjacencyList)
    
    
    #def AddVertex(self, vertex):
    #    self.vertexList.append(vertex) # [vertex_1: [], vertex_2: [], ...]
    #    
    #def AddVertexList(self, vertexList):
    #    self.vertexList = vertexList
    #    
    #def AddUndirectedEdge(self, vertex_a, vertex_b, weight):
    #    self.AddDirectedEdge(vertex_a, vertex_b, weight)
    #    self.AddDirectedEdge(vertex_b, vertex_a, weight)
    #
    #def AddDirectedEdge(self, fromVertex, toVertex, weight):
    #    self.edgeWeights.append((fromVertex, toVertex, weight))
        
    #Use the list of vertices, add undirected edges from each vertex to each other vertex and 
    # their edge weight in the following format: [(vertex1, vertex2, edgeWeight), (vertex2, vertex3, edgeWeight)]
    #def AddEdges(self, edgeData):
        
    
    #Add the Vertex whose address matches the package address to the truck route list.
    #def AddVerticesFromPackageList(self, packageList):
    #    truckRouteVertexList = []
    #    
    #    truckRouteVertexList.append(self.vertexList[0]) #Start at the hub
    #    
    #    for package in packageList:
    #        truckRouteVertexList.append(package.vertex)
    #                
    #    
    #    #truckRouteVertexList.append(self.vertexList[0]) #Finish at the hub
    #    
    #    return truckRouteVertexList
    
    #This takes a list of packages on a truck .
    #def FindRoute(self, packageList):
    #    truckRouteList = self.AddVerticesFromPackageList(packageList)
    #    
    #    smallestEdgeWeight = float(10**50)
    #    distanceTraveled = float(0)
    #    
    #    #TODO: This function needs to simply return a list of vertices in the order they should be visited.
    #    while(packageList):
    #        
    #        #for i, current_Vertex in truckRouteList:
    #        #    if i == 0:
    #        #        continue
    #            
    #            
    #        for i, package in enumerate(packageList): #Put the package vertices into the truck route list.
    #            for key, value in package.vertex.edgesList.items():
    #                if value != 0 and value < smallestEdgeWeight:
    #                    smallestEdgeWeight = value
    #                    distanceTraveled += value
    #                    print()
    #            truckRouteList.append(key)
    #            packageList.remove(package)
    #            
    #            #truckRouteList.append(package.vertex)
    #   
    #    #truckRouteList.append(self.vertexList[0]) #finish at the hub
        
    #TODO: return a list of vertices in the order the truck will 
    # deliver the packages according to nearest Neighbor algorithm
    
    