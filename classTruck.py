from datetime import datetime, time, timedelta
from classGraph import Graph
from classPackage import Package
from classAdjacencyMatrix import AdjacencyMatrix

class Truck:
    def __init__(self, p_id, p_startDateTime = datetime.combine(datetime.today(), time(8, 0))):
        self.id = p_id
        self.packageList = []
        #self.packageToVertexList = [] # [(package, vertex), (package, vertex)]
        self.startingAddress = 'HUB' #Initalize to the starting address, which is the 'HUB'
        self.currentAddress = None 
        self.currentPackage = object()
        self.milesTraveled = 0
        self.isAllPackagesDelivered = False
        self.startDateTime = p_startDateTime
        self.currentdateTime = p_startDateTime #TODO: Create a startTime Attribute for leaving time. Elapsed time for how long it takes to deliver packages. Set the third truck start time at the time that is earlier between the two previous trucks.
        self.elapsedTime = None
        self.adjacencyMatrix = []
        self.remainingPackageNum = 0
        self.speed = 18
        
    def AddPackageList(self, packageList):
        self.packageList = packageList
        
    def AddPackage(self, package):
        self.packageList.append(package)
        return True
    
    def DeliverPackages(self, p_adjacencyMatrix):
        self.adjacencyMatrix = p_adjacencyMatrix
        self.remainingPackageNum = len(self.packageList)
        
        print(f'----- Truck {self.id}: starting @ {self.startingAddress}, current time: {self.currentdateTime.time()} -----')
        
        #Base case: Current address is NULL. Find the next closest package to the starting address. 
        self.currentAddress = self.startingAddress
        nextPackage = self.FindClosestUndeliveredPackage()
        
        if nextPackage:
            self.DeliverPackage(nextPackage)
            
        while not self.isAllPackagesDelivered: #TODO: This logic alone will not confirm all packages have been delivered. Perhaps a final loop at the end?
            nextPackage = self.FindClosestUndeliveredPackage()
            
            if nextPackage:
                self.DeliverPackage(nextPackage)
            else:
                self.isAllPackagesDelivered = True
        
    def DeliverPackage(self, package):
        self.currentPackage = package #Set currentPackage to the next packageObj in packageList.
        self.currentAddress = package.address #The adjacency matrix needs addresses to determine distances for the next closest package.
        package.isDelivered = True
        self.remainingPackageNum -= 1
        print(f'Delivered package: {package.id} @ {self.currentAddress}, current mileage: {self.milesTraveled:.2f}, current time: {self.currentdateTime.time()} ---> ')
        
    #Iterate through the address list finding the next closest package to deliver.
    def FindClosestUndeliveredPackage(self):
        shortestDistance = float('inf')
        closestPackage = None
        
        for package in self.packageList: #Iterate through all packages
            if package.isDelivered == False:
                distance = AdjacencyMatrix.FindDistanceBetweenAddresses(self.currentAddress, package.address)
                if distance is not None and distance != 0 and distance < shortestDistance:
                    shortestDistance = distance
                    closestPackage = package
                    
        if closestPackage is not None: #If closestPackage has a value, we are not at the end of the package list.
            self.milesTraveled += shortestDistance
            travelTimeMinutes = round((shortestDistance / self.speed) * 60) #Find the travel time. Round to take out seconds.
            self.currentdateTime += timedelta(minutes=travelTimeMinutes) #Add the travel time to the current time.
            closestPackage.deliveryTime = self.currentdateTime.time()
        
        return closestPackage
    