'''
This  Program is called Space Finder. To help Traverllers.

Author : Aryan
Date : 20 JuL 2020
'''

# Welcome Message
print("Hello, I am your space finder")
name = input("what is your name: ")
print("Hello %s, How are you doing"%(name))

# Identifying the traveller
namee = input("Which planet are you from, you cute little alien:")
if (namee.strip()).lower() == "earth":
    print("It means that you are a human")
elif (namee.strip()).lower() == "mercury" :
    print("It means that you are from mercury")
elif (namee.strip()).lower() == "venus" :
    print("It means that you are from venus")
elif (namee.strip()).lower() == "mars" :
    print("It means that you are from mars")
elif (namee.strip()).lower() == "jupiter" :
    print("It means that you are from jupiter")
elif (namee.strip()).lower() == "saturn" :
    print("It means that you are from saturn")
elif (namee.strip()).lower() == "uranus" :
    print("It means that you are from uranus")   
elif (namee.strip()).lower() == "neptune" :
    print("It means that you are from neptune")                           
else:
    print("I have never heard of %s planet in my family. Try another place"%namee)
    

# Take a request to Travel
place = input("which planet do you want to travel in the solar system: ") 


############ Validating the Travel request #############

## Travel FROM EARTH to Other Planets
if (namee.strip()).lower() == 'earth' and (place.strip()).lower() == 'mercury':
    print("91,691,000km is the distance from earth to mercury")
    

elif (namee.strip()).lower() == 'earth' and (place.strip()).lower() == 'venus':
    print("41,400,000km is the distance from from earth to venus")
    print("")   

elif (namee.strip()).lower() == 'earth' and (place.strip()).lower() == 'mars': 
    print("78,340,000km is the distance from earth to mars")
ck

elif (namee.strip()).lower() == 'earth' and (place.strip()).lower() == 'jupiter':
    print("628,730,000km is the distance from earth to jupiter")
    print("")
elif (namee.strip()).lower() == 'earth' and (place.strip()).lower() == 'saturn':
    print("1,275,000,000km is the distancevfrom earth to saturn")
    print("")
elif (namee.strip()).lower() == 'earth' and (place.strip()).lower() == 'uranus':
    print("2,723,950,000km is the distance from earth to uranus")
    print("")

elif (namee.strip()).lower()  == 'earth' and (place.strip()).lower() == 'neptune':
    print('4,351,400,000km is the distance from earth to neptune')
    print("")


## Travel FROM MERCURY to Other Planets
if (namee.strip()).lower() == 'mercury' and (place.strip()).lower() == 'earth':
    print("91,691,000km is the distance from mercury to earth")


elif (namee.strip()).lower() == 'mercury' and (place.strip()).lower() == 'venus':
    print("50,290,000km is the distance from mercury to venus")

elif (namee.strip()).lower() == 'mercury' and (place.strip()).lower() == 'mars': 
    print("170,030,000km is the distance from mercury to mars")

elif (namee.strip()).lower() == 'mercury' and (place.strip()).lower() == 'jupiter':
    print("720,420,000km is the distance from mercury to jupiter")

elif (namee.strip()).lower() == 'mercury' and (place.strip()).lower() == 'saturn':
    print("1,366,690,000km is the distance from mercury to saturn")

elif (namee.strip()).lower() == 'mercury' and (place.strip()).lower() == 'uranus':
    print("2,815,640,000km is the distance from mercury to uranus")
    
elif (namee.strip()).lower()  == 'mercury' and (place.strip()).lower() == 'neptune':
    print('4,443,090,000km is the distance from mercury to neptune')


## Travel FROM VENUS to Other Planets
if (namee.strip()).lower() == 'venus' and (place.strip()).lower() == 'earth':
    print("41,400,000km is the distance from venus to earth")
    
elif (namee.strip()).lower() == 'venus' and (place.strip()).lower() == 'mercury':
    print("50,290,000km is the distance from venus to mercury")

elif (namee.strip()).lower() == 'venus' and (place.strip()).lower() == 'mars': 
    print("119,740,000km is the distance from venus to mars")

elif (namee.strip()).lower() == 'venus' and (place.strip()).lower() == 'jupiter':
    print("670,130,000km is the distance from venus to jupiter")

elif (namee.strip()).lower() == 'venus' and (place.strip()).lower() == 'saturn':
    print("1,316,400,000km is the distance from venus to saturn")

elif (namee.strip()).lower() == 'venus' and (place.strip()).lower() == 'uranus':
    print("2,765,350,000km is the distance from venus to uranus")

elif (namee.strip()).lower()  == 'venus' and (place.strip()).lower() == 'neptune':
    print('4,392,800,000km is the distance from venus to neptune')


## Travel FROM MARS to Other Planets
if (namee.strip()).lower() == 'mars' and (place.strip()).lower() == 'earth':
    print("78,340,000km is the distanc from mars to earth")

elif (namee.strip()).lower() == 'mars' and (place.strip()).lower() == 'mercury':
    print("170,030,000km is the distance from mars to mercury")

elif (namee.strip()).lower() == 'mars' and (place.strip()).lower() == 'venus': 
    print("119,740,000km is the distance from mars to venus")

elif (namee.strip()).lower() == 'mars' and (place.strip()).lower() == 'jupiter':
    print("4,392,800,000km is the distance from mars to jupiter")

elif (namee.strip()).lower() == 'mars' and (place.strip()).lower() == 'saturn':
    print("1,196,660,000km is the distance from mars to saturn")

elif (namee.strip()).lower() == 'mars' and (place.strip()).lower() == 'uranus':
    print("2,645,610,000km is the distance from mars to uranus")

elif (namee.strip()).lower()  == 'mars' and (place.strip()).lower() == 'neptune':
    print('4,273,060,000km is the distance from mars to neptune')


## Travel FROM JUPITER to Other Planets
if (namee.strip()).lower() == 'jupiter' and (place.strip()).lower() == 'earth':
    print("628,730,000km is the distance from jupiter to earth")

elif (namee.strip()).lower() == 'jupiter' and (place.strip()).lower() == 'mercury':
    print("720,420,000km is the distance from jupiter to mercury")

elif (namee.strip()).lower() == 'jupiter' and (place.strip()).lower() == 'venus': 
    print("670,130,000km is the distance from jupiter to venus")

elif (namee.strip()).lower() == 'jupiter' and (place.strip()).lower() == 'mars':
    print("4,392,800,000km is the distance from jupiter to mars")

elif (namee.strip()).lower() == 'jupiter' and (place.strip()).lower() == 'saturn':
    print("646,270,000km is the distance from jupiter to saturn")

elif (namee.strip()).lower() == 'jupiter' and (place.strip()).lower() == 'uranus':
    print("2,095,220,000km is the distance from jupiter to uranus")

elif (namee.strip()).lower()  == 'jupiter' and (place.strip()).lower() == 'neptune':
    print('3,722,670,000km is the distance from jupiter to neptune')


## Travel FROM SATURN to Other Planets
if (namee.strip()).lower() == 'saturn' and (place.strip()).lower() == 'earth':
    print("1,275,000,000km is the distance from saturn to earth")

elif (namee.strip()).lower() == 'saturn' and (place.strip()).lower() == 'mercury':
    print("1,366,690,000km is the distance from saturn to mercury")

elif (namee.strip()).lower() == 'saturn' and (place.strip()).lower() == 'venus': 
    print("1,316,400,000km is the distance from saturn to venus")

elif (namee.strip()).lower() == 'saturn' and (place.strip()).lower() == 'mars':
    print("1,196,660,000km is the distance from saturn to mars")

elif (namee.strip()).lower() == 'saturn' and (place.strip()).lower() == 'jupiter':
    print("646,270,000km is the distance from saturn to jupiter")

elif (namee.strip()).lower() == 'saturn' and (place.strip()).lower() == 'uranus':
    print("1,448,950,000km is the distance from saturn to uranus")

elif (namee.strip()).lower()  == 'saturn' and (place.strip()).lower() == 'neptune':
    print('is the distance from saturn to neptune')


## Travel FROM URANUS to Other Planets
if (namee.strip()).lower() == 'uranus' and (place.strip()).lower() == 'earth':
    print("2,723,950,000km is the distance from uranus to earth")
elif (namee.strip()).lower() == 'uranus' and (place.strip()).lower() == 'mercury':
    print("2,815,640,000km is the distance from uranus to mercury")
elif (namee.strip()).lower() == 'uranus' and (place.strip()).lower() == 'venus': 
    print("2,765,350,000km is the distance from uranus to venus")
elif (namee.strip()).lower() == 'uranus' and (place.strip()).lower() == 'mars':
    print("2,645,610,000km is the distance from uranus to mars")
elif (namee.strip()).lower() == 'uranus' and (place.strip()).lower() == 'jupiter':
    print("2,095,220,000km is the distance from uranus to jupiter")
elif (namee.strip()).lower() == 'uranus' and (place.strip()).lower() == 'saturn':
    print("1,448,950,000km is the distance from uranus to saturn")
elif (namee.strip()).lower()  == 'uranus' and (place.strip()).lower() == 'neptune':
    print('1,627,450,000km is the distance from uranus to neptune')


## Travel FROM NEPTUNE to Other Planets
if (namee.strip()).lower() == 'neptune' and (place.strip()).lower() == 'earth':
    print("4,351,400,000km is the distance from neptune to earth")
elif (namee.strip()).lower() == 'neptune' and (place.strip()).lower() == 'mercury':
    print("4,443,090,000km is the distance from neptune to mercury")
elif (namee.strip()).lower() == 'neptune' and (place.strip()).lower() == 'venus': 
    print("4,392,800,000km is the distance from neptune to venus")
elif (namee.strip()).lower() == 'neptune' and (place.strip()).lower() == 'mars':
    print("4,273,060,000km is the distance from neptune to mars")
elif (namee.strip()).lower() == 'neptune' and (place.strip()).lower() == 'jupiter':
    print("3,722,670,000km is the distance from neptune to jupiter")
elif (namee.strip()).lower() == 'neptune' and (place.strip()).lower() == 'saturn':
    print("3,076,400,000km is the distance from neptune to saturn")
elif (namee.strip()).lower()  == 'neptune' and (place.strip()).lower() == 'uranus':
    print('1,627,450,000km is the distance from neptune to uranus')