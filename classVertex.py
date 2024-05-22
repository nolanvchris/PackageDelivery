
class Vertex:
    def __init__(self):
        self.address = ''
        self.edgesList = {} # dictionary (order matters) {vertex1: distance1, vertex2: distance2}
        self.packageId = -1
        
    def __str__(self):
        return "%s, %s" % (self.address, self.edgesList)
        
    def AddEdge(self, vrtx, distance):
        self.edgesList[vrtx] = distance
        
    #def IsVertexAdjacent(self, vertex)
    #return 
    