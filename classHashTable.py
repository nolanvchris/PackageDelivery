class HashTable:
    def __init__(self, numOfBuckets = 10):
        self.hashTable = []
        for i in range(numOfBuckets):
            self.hashTable.append([])
        
    def hash_function(self, key):
        return hash(key) % len(self.hashTable)
        
    def insert(self, key, value): #key = packageId, value = [address, city...]
        bucketIndex = self.hash_function(key)
        bucketList = self.hashTable[bucketIndex]
        
        for element in bucketList: #Check list to see if the key already exists, if so update the value.
            if element[0] == key:
                element[1] = value
                return True 
            
        keyValue = [key, value] # The for loop above determined the list does not contain the key, therefore add key_value pair to the end of the list.
        bucketList.append(keyValue) 
        return True
    
    def lookUp(self, key): # Return the value of a given key from the hash table.
        bucketIndex = self.hash_function(key)
        bucketList = self.hashTable[bucketIndex]
        
        for element in bucketList: # Iterate through the bucket list to find the key, return the corresponding value.
            if element[0] == key:
                return element[1]
        return None
    
    def displayHashTableData(self): #numOfEntries): 
        #i = 1
        #while i <= numOfEntries:
        #    print(self.lookUp(i))
        #    i += 1
        #print(f"\n--------------Hash Table Data consists of {numOfEntries} entries--------------\n")
        
        for bucket in self.hashTable:
            for bucketListObject in bucket:
                print(bucketListObject)