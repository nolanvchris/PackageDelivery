class Package:
    def __init__(self, p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weightKilo, p_specialNotes):
        self.id = int(p_id)
        self.address = p_address
        self.city = p_city
        self.state = p_state
        self.zip = p_zip
        self.deadline = p_deadline
        self.weightKilo = int(p_weightKilo)
        self.specialNotes = p_specialNotes
        self.isDelivered = False
        self.deliveryTime = None
        #self.vertex = vertex
        
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.address, self.city, self.state, self.zip, self.deadline, self.weightKilo, self.specialNotes)
    
    #def AddVertexToCorrespondingPackage(self, vertex):