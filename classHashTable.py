from datetime import datetime, time

class HashTable:
    def __init__(self, numOfBuckets = 10):
        self.hashTable = []
        for i in range(numOfBuckets):
            self.hashTable.append([]) #Append empty buckets to a list [[],[],[]...]
        
    #This function is similar to an internal class function that can be used by other class functions to hash key values.
    def hash_function(self, key):
        return hash(key) % len(self.hashTable) 
        
    def insert(self, key, value): #key = packageId, value = [address, city...]
        bucketIndex = self.hash_function(key)
        bucketList = self.hashTable[bucketIndex]
        
        for element in bucketList: #Check bucket list to see if the key already exists, if so update the value.
            if element[0] == key:
                element[1] = value
                return True 
            
        keyValue = [key, value] 
        
        #Change the Deadlines 0.4375 and 0.375 to 10:30am and 9am respectively.
        if keyValue[1].deadline == '0.4375':
            keyValue[1].deadline = datetime.combine(datetime.today(), time(10, 30))
        elif keyValue[1].deadline == '0.375':
            keyValue[1].deadline = datetime.combine(datetime.today(), time(9, 0))
            
        bucketList.append(keyValue) #The for loop above determined the list does not contain the key, therefore add key_value pair to the end of the list.
        return True
    
    def lookUp(self, key): # Return the value of a given key from the hash table.
        bucketIndex = self.hash_function(key)
        bucketList = self.hashTable[bucketIndex]
        
        for element in bucketList: # Iterate through the bucket list to find the key, return the corresponding value.
            if element[0] == key:
                return element[1]
        return None
    
    #This code was created to see if data was getting loaded into the hash table properly.
    def displayHashTableData(self):
        for bucket in self.hashTable:
            for bucketListObject in bucket:
                print(bucketListObject)