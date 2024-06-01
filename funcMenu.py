
from datetime import datetime, time

#Total time complexity: O(n^2) as trucks and packages increase
def menu(p_truckFleetList, p_hashTable_packageData):
    
        #Start a loop for selecting a correct menu option.
        while True:
            userInput = None
            
            #display options
            print('\n-----Select an option----- \n')
            print('Press 1 to: Display all package information at a specified time')
            print('Press 2 to: Display package information on specific package')
            print('Press 3 to: Display mileage of trucks')
            print('To exit press: 0\n')
            
            userInput = input('> ')
            
            #Validate user input
            try:
                userInput = int(userInput)
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue #Prompt the user again if the selection is invalid.
            
            if userInput == 1:
                
                #Start a loop for inputing a correct inquiry time.
                while True:
                    print('\nEnter a time in the format HH:MM. For example 10:30')
                    inquiryTime = input('> ')

                    #Attempt to correctly parse the user input and return a datetime object.
                    try:
                        hours, minutes = parseTime(inquiryTime)
                        inquiryDateTime = datetime.combine(datetime.today(), time(hours, minutes))
                        break  #Exit the loop if the time is valid
                    except ValueError as e:
                        print(e)
                        continue  #Prompt the user again if the time is invalid.
                
                #O(n^2) as trucks and packages increase
                for truck in p_truckFleetList:
                    print(f'\n-------------------- Truck {truck.id} starting at: {truck.startingAddress}, start time: {truck.startDateTime.time()} --------------------')
                    
                    for package in truck.packageList:
                        
                        #Update the wrong address at the correct time.
                        if package.specialNotes == 'Wrong address listed' and inquiryDateTime >= truck.startDateTime:
                            truck.updateWrongAddress(package)
                        
                        #These if statements determine what the package status should be at given time intervals.
                        if package.specialNotes == 'Delayed on flight---will not arrive to depot until 9:05 am' and inquiryDateTime < truck.startDateTime: #if True, package has not arrived at the hub yet.
                            package.status = 'Awaiting package arrival'
                        elif inquiryDateTime <= truck.startDateTime: #Time interval before the truck has left. if True Package should be at the 'HUB'
                            package.status = truck.startingAddress
                        elif inquiryDateTime > truck.startDateTime and inquiryDateTime < package.deliveryDateTime: #Time interval after the truck has started deliveries but before package has been delivered. If true package is 'Enroute'
                            package.status = 'Enroute'
                        elif inquiryDateTime >= package.deliveryDateTime: #Time interval after package has been delivered. If true package has been 'Delivered'.
                            package.status = 'Delivered'

                        #Special cases: deadline is either a string or a datetime object. delivery time is either included or not.
                        deadline = package.deadline if package.deadline == 'EOD' else package.deadline.strftime('%H:%M:%S')
                        delivery_time = f'@ {package.deliveryDateTime.time()}' if package.status == 'Delivered' else ''

                        print(f'Truck No. {truck.id:<2} Package ID: {package.id:<3} Address: {package.address:<39} Deadline: {deadline:<9} Status: {package.status:<9} {delivery_time}')

            elif userInput == 2:

                while True:
                    try:
                        print('\nEnter a package ID between 1 and 40')
                        packageIdInquiry = int(input('> ')) #Check that a number was entered.
                        
                        if 1 <= packageIdInquiry <= 40: #Check that the number en
                            break
                        else:
                            print("ID does not exist. Please enter an ID between 1 and 40.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        
                print(p_hashTable_packageData.lookUp(packageIdInquiry))

            elif userInput == 3:
                #Get total miles traveled for all trucks.
                totalMilesForAllTrucks = float()
                for truck in p_truckFleetList:
                    totalMilesForAllTrucks += truck.milesTraveled
                    print(f'truck no. {truck.id:<2} mileage: {truck.milesTraveled}')
                print(f'\nTotal distance traveled for all trucks is: {totalMilesForAllTrucks:.2f} miles')
            
            elif userInput == 0: #Exit Menu
                break
                         
def parseTime(inquiryTime):
    
    #Parses a time string in the format HH:MM and returns a tuple (hours, minutes).
    #Raises ValueError if the format is incorrect or the time is invalid.
    try:
        parsedTime = datetime.strptime(inquiryTime, '%H:%M').time()
        return parsedTime.hour, parsedTime.minute
    except ValueError:
        raise ValueError('Time must be in the format HH:MM and be a valid time.')