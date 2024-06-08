from datetime import datetime, time, timedelta
from classAdjacencyMatrix import AdjacencyMatrix

class Truck:
    def __init__(self, p_id, p_startDateTime = datetime.combine(datetime.today(), time(8, 0))):
        self.id = p_id
        self.packageList = []
        self.startingAddress = 'HUB' #Initalize to the starting address, which is the 'HUB'
        self.currentAddress = None 
        self.currentPackage = None
        self.milesTraveled = 0
        self.isAllPackagesDelivered = False
        self.startDateTime = p_startDateTime
        self.currentDateTime = None
        self.elapsedTime = None
        self.remainingPackageNum = 0
        self.speed = 18
        self.status = None
        
    #This function takes a list of package objects and loads them on truck through the AddPackage() function.
    def AddPackageList(self, packageList):
        for package in packageList:
            self.AddPackage(package)
    
    #Load package onto the truck.packageList
    def AddPackage(self, package):
        package.status = 'HUB' #Package now at the 'HUB'
        package.truckId = self.id #Package is loaded onto a specific truck with corresponding ID
        self.packageList.append(package)
        return True
    
    #Deliver truck packages according to the nearest neighbor algorithmn.
    def DeliverPackages(self):
        self.remainingPackageNum = len(self.packageList) #Track remaining packages left to deliver.
        self.currentDateTime = self.startDateTime
        
        self.status = 'Delivering packages' #Truck status set to delivering packages.
        
        #O(n), Starting delivery route. Set packages' statuses to 'enroute'.
        for package in self.packageList: 
            package.status = 'enroute'
        
        #Base case: Current address is initialized to 'HUB'. Find the next closest package to the starting address. 
        self.currentAddress = self.startingAddress
        nextPackage = self.FindClosestUndeliveredPackage()
        
        #Closest package from the 'HUB' was found. Now deliver it.
        if nextPackage:
            self.DeliverPackage(nextPackage)
            
        #O(n^2), Enter a loop to deliver the rest of the packages.
        while not self.isAllPackagesDelivered:
            nextPackage = self.FindClosestUndeliveredPackage()
            
            if nextPackage:
                self.DeliverPackage(nextPackage) #send 'nextPackage' to the DeliverPackage function to be delivered.
            else:
                self.isAllPackagesDelivered = True
                
        self.ReturnToTheHub() #After all packages have been delivered return to the hub.

    def DeliverPackage(self, deliveryPackage):
        self.currentPackage = deliveryPackage #For the next DeliverPackages() iteration, currentPackage is set to deliveredPackage.
        self.currentAddress = deliveryPackage.address #The adjacency matrix needs the current trucks address to determine where the next closest package is.
        deliveryPackage.isDelivered = True
        deliveryPackage.status = 'Delivered'
        self.remainingPackageNum -= 1
        #package.truckMileageAtDelivery = self.milesTraveled

    #Function total time complexity: for loop O(n) + FindDistanceBetweenAddresses O(n)
    def FindClosestUndeliveredPackage(self):
        shortestDistance = float('inf')
        closestPackage = None
        
        #O(n), Iterate through the packageList list finding the next closest package to deliver.
        for package in self.packageList:
            if package.isDelivered == False: #make sure we are not trying to deliver a package we have already delivered.
                distance = AdjacencyMatrix.FindDistanceBetweenAddresses(self.currentAddress, package.address)
                if distance is not None and distance < shortestDistance: #check that a distance was returned, and see if it was less than the other distances.
                    shortestDistance = distance
                    closestPackage = package
                    
        if closestPackage is not None: #Check if next closest package was found.
            self.milesTraveled += shortestDistance #Keep track of the trucks current mileage.
            
            #Update the current time based on the distance traveled and the rate of speed.
            travelTimeMinutes = round((shortestDistance / self.speed) * 60)
            self.currentDateTime += timedelta(minutes=travelTimeMinutes) 
            closestPackage.deliveryDateTime = self.currentDateTime #package object will track when it was delivered.
        
        return closestPackage
    
    #O(1)
    def ReturnToTheHub(self):
        distance = AdjacencyMatrix.FindDistanceBetweenAddresses(self.currentAddress, self.startingAddress)
        self.milesTraveled += distance
        self.currentAddress = self.startingAddress
        self.status = 'Route Complete' #Truck is back at the hub, route complete. 
        
    def updateWrongAddress(self, package):
        package.address = '410 S State St'
        package.city = 'Salt Lake City'
        package.state = 'UT'
        package.zip = '84111'