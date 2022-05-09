#NJW Missing comments at top of file (-0.5)
#NJW 9.5/10

#Task 3
coursesTaken = int(input('Enter number of courses taken here: '))

if coursesTaken <= 9:
    studentYear = 'Freshman'

elif coursesTaken < 17:
    studentYear = 'Sophomore'

elif coursesTaken < 25:
    studentYear = 'Junior'

else:
    studentYear = 'Senior'

print('You are a:',studentYear)


#Task 4
speedLimit = int(input('Enter speed limit here:'))
clockedSpeed = int(input('Enter clocked speed here:'))
amountOverLimit = (clockedSpeed - speedLimit)

# 50 + 5/mph, 300 any over 80

if clockedSpeed > 80:
    ticketPrice = 300 + 50 + (amountOverLimit * 5)
    print('Your ticket amount is:', ticketPrice)

elif clockedSpeed > speedLimit < 80:
    ticketPrice = 50 + (amountOverLimit * 5)
    print('Your ticket amount is:',ticketPrice)

else:
    print('Your speed is legal, no ticket for you')



#Task 5
month = int(input('Enter month here:'))
day = int(input('Enter day here:'))
year = int(input('Enter year here:'))


if month < 1:
    print('invalid month, please enter a value 1-12')
    
elif month > 12:
    print('invalid month, please enter a value 1-12')
    
elif day < 1:
    print('invalid day, please enter a value 1-31')
    
elif day > 31:
    print('invalid day, please enter a value 1-31')
    
elif year < 0:
    print('invalid year, please enter a value 0-9990')
    
elif year > 9999:
    print('invalid year, please enter a value 0-9999')
else:
    print('Date is valid')



# Task 6
partyPeople = int(input('Quantity of people attending the party: '))
hotDogsPerGuest = int(input('Quantity of hot dogs per guest: '))
hotDog = 10
buns = 8

if partyPeople <= 10:
    hotDogPackages = 1

elif partyPeople % 10 == 0:
    hotDogPackages = (partyPeople * hotDogsPerGuest) / hotDog

elif partyPeople > 10:
    hotDogPackages = ((partyPeople * hotDogsPerGuest) // hotDog) + 1

print('Quantity of hot dog packages needed:',int(hotDogPackages))


if partyPeople <= 8:
    bunPackages = 1

elif partyPeople % 8 == 0:
    bunPackages = (partyPeople * hotDogsPerGuest) / buns

elif partyPeople > 8:
    bunPackages = ((partyPeople * hotDogsPerGuest) // buns) + 1

print('Quantity of bun packages needed:',bunPackages)

totalHotDogs = hotDog * hotDogPackages
hotDogsNeeded = partyPeople * hotDogsPerGuest
totalBuns = buns * bunPackages
bunsNeeded = partyPeople * hotDogsPerGuest
hotDogsRemaining = totalHotDogs % hotDogsNeeded
bunsRemaining = totalBuns % bunsNeeded

if totalHotDogs > hotDogsNeeded:
    print('Hot dogs remaining: ',hotDogsRemaining)
else:
    print('There will be no remaining hot dogs.')

if totalBuns > bunsNeeded:
    print('Buns remaining:',bunsRemaining)
else:
    print('There will be no remaining buns')

