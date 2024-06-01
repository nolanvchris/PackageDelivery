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
        self.deliveryDateTime = None
        self.status = 'N/A'
        self.truckId = None #track which truck the package is on.
        
    def __str__(self):
        return "Address: %s %s %s %s  Weight: %s  Deadline: %s  Status: %s" % (self.address, self.city, self.state, self.zip, self.weightKilo, self.deadline, self.status)