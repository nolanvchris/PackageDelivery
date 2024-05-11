
class Graph:
    def __init__(self):
        self.adjacencyList = {}
        self.edgeWeights = {}
        
    def __str__(self):
        return "%s\n" % (self.adjacencyList)
        
    def AddVertex(self, vertex):
        self.adjacencyList[vertex] = [] # {vertex_1: [], vertex_2: [], ...}
        
    def AddDirectedEdge(self, fromVertex, toVertex, weight):
        self.edgeWeights[(fromVertex, toVertex)] = weight #ex. {(vertex_1, vertex_2): 251, (vertex_1, vertex_3): 541...}
        self.adjacencyList[fromVertex].append(toVertex) #This dictionary contains info on how far vertexs are from eachother
        
    def AddUndirectedEdge(self, adjVertex_a, adjVertex_b, weight):
        self.AddDirectedEdge(adjVertex_a, adjVertex_b, weight)
        self.AddDirectedEdge(adjVertex_b, adjVertex_a, weight)
        
    
    
    # [] Node 1: "International Peace Gardens 1060 Dalton Ave S"
    # [] Node 2: "International Peace Gardens 1060 Dalton Ave S"
    # [] Node 3: "International Peace Gardens 1060 Dalton Ave S"
    # [] Node 4: "International Peace Gardens 1060 Dalton Ave S"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Dijkstra shortest path
def dijkstra_shortest_path(g, start_vertex):
    # Put all vertices in an unvisited queue.
    unvisited_queue = []
 
    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex) 
            # unvisited_queue = [vertex_1, vertex_2, ...]
 
    # Start_vertex has a distance of 0 from itself
    start_vertex.distance = 0
 
    # One vertex is removed with each iteration; repeat until the list is
    # empty.
    while len(unvisited_queue) > 0:
        
        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            #print(unvisited_queue[i].label, unvisited_queue[i].distance, unvisited_queue[i].pred_vertex)
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)
        #print("From Start Vetex to current_vertex.label: " + current_vertex.label +" distance: " + str(current_vertex.distance))
 
        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in g.adjacency_list[current_vertex]: # values from  dictionary
                # if current_vertex = vertex_1 => adj_vertex in [vertex_2, vertex_3], if vertex_2 => adj_vertex in [vertex_6], ...
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)] # values from dictionary
                # edge_weight = 484 then 626 then 1306, ...}
            alternative_path_distance = current_vertex.distance + edge_weight
                        
            # If shorter path from start_vertex to adj_vertex is found, update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex
                
def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = " -> " + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path
 
def get_shortest_path_city(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        myMovie = myHash.search(int(current_vertex.label))
        path = " -> " + myMovie.city + path
        current_vertex = current_vertex.pred_vertex
    path = "Salt Lake City " + path
    return path
