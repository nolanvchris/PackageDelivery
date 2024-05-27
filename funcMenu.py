
from datetime import datetime, time

def menu(p_truckFleetList):
    
        #Start a loop for selecting a correct menu option.
        while True:
            userInput = None
            
            #display options
            print('\n-----Select an option----- \n')
            print('Press 1 to: Display package information at a specified time')
            print('Press 2 to: Display total mileage of all trucks')
            print('To exit press: 0\n')
            
            userInput = input('> ')
            
            #Validate user input
            try:
                userInput = int(userInput)
            except ValueError:
                print("Invalid input. Please enter a number.")
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
                
                for truck in p_truckFleetList:
                    print(f'\n----- Truck {truck.id} starting at: {truck.startingAddress}, start time: {truck.startDateTime.time()} -----')
                    
                    #These if statements determine what the package status should be at given time intervals.
                    for package in truck.packageList:
                        if package.specialNotes == 'Delayed on flight---will not arrive to depot until 9:05 am' and inquiryDateTime < truck.startDateTime: #if True, package has not arrived at the hub yet.
                            package.status = 'Awaiting package arrival'
                        elif inquiryDateTime <= truck.startDateTime: #Time interval before the truck has left. if True Package should be at the 'HUB'
                            package.status = truck.startingAddress
                        elif inquiryDateTime > truck.startDateTime and inquiryDateTime < package.deliveryDateTime: #Time interval after the truck has started deliveries but before package has been delivered. If true package is 'Enroute'
                            package.status = 'Enroute'
                        elif inquiryDateTime >= package.deliveryDateTime: #Time interval after package has been delivered. If true package has been 'Delivered'.
                            package.status = 'Delivered'

                        #If a package has been delivered we want to include the time it was delivered.
                        if package.status == 'Delivered':
                            print(f'Package ID: {package.id:<3} Address: {package.address:<39} Status: {package.status:<10} @ {package.deliveryDateTime.time()}')
                        else:
                            print(f'Package ID: {package.id:<3} Address: {package.address:<39} Status: {package.status:<10}')

            elif userInput == 2:
                #Get total miles traveled for all trucks.
                totalMilesForAllTrucks = float()
                for truck in p_truckFleetList:
                    totalMilesForAllTrucks += truck.milesTraveled
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