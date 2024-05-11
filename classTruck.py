from datetime import time
class Truck:
    def __init__(self, packageList, isRouteComplete):
        self.packageList = packageList
        self.mileage = int()
        self.isRouteComplete = isRouteComplete
        self.truckTime = time()