class AdjacencyMatrix:
    
    adjacencyMatrix = []
        
    @classmethod
    def set_matrix(cls, adjacencyMatrix):
        cls.adjacencyMatrix = adjacencyMatrix
    
    @classmethod
    def get_matrix(cls):
        return cls.adjacencyMatrix
    
    @classmethod
    def FindDistanceBetweenAddresses(cls, from_address, to_address):
        for i, row in enumerate(cls.adjacencyMatrix):
            if i > 1 and row[1] == from_address:
                
                for j, col in enumerate(row):
                    if cls.adjacencyMatrix[1][j] == to_address:
                        distance = float(cls.adjacencyMatrix[i][j])
                        return distance