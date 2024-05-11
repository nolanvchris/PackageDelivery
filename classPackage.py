class Package:
    def __init__(self, address, city, state, zip, deadline, weightKilo, specialNotes):
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weightKilo = weightKilo
        self.specialNotes = specialNotes
        self.isDelivered = False
        
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.address, self.city, self.state, self.zip, self.deadline, self.weightKilo, self.specialNotes)