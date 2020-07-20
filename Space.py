
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
elif (namee.strip()).lower() == "Uranus" :
    print("It means that you are from uranus")   
elif (namee.strip()).lower() == "Neptune" :
    print("It means that you are from neptune")                           
else:
    print("I have never heard of %s planet in my family. Try another place"%namee)


# Take a request to Travel
place = input("which planet do you want to travel in the solar system: ") 


# Validating the Travel request
if place == "mercury" or "Mercury" and namee == "earth" or "Earth":    
        print(" Mercury is 115.36 million km away from earth and if you are traveling in 140,000 mph, it can take up to 6 and a half years to reach your desired location")

if place == "venus" or "Venus" and namee == "earth" or "Earth":    
        print("Venus is 76.15 million km away from earth and is you travel 12000mph, it can take 15 months to reach your desired location")        

if place == "Mars" or "mars" and namee == "earth" or "Earth":    
        print("106.35 million km is the distance from earth to mars and it would take roughly 8 months to reach your desired location depending on which spacecraft you are travelling with.")
        
if place == "Jupiter" or "jupiter" and namee == "earth" or "Earth":    
        print("620.25 million km is the distance from earth to jupiter and it would take 13 months to reach your desired location")
        
if place == "Uranus" or "uranus" and namee == "earth" or "Earth":    
        print("It would take around 3 to 4 yers to reach there because it 2.9895 billion km away from your home planet")
        
if place == "neptune" or "Neptune" and namee == "earth" or "Earth":    
        print("4.3826 billion km is the distance from earth of neptune and it would take 8 years to reach there ")
       
if place == "Saturn" or "saturn" and namee == "earth" or "Earth":    
        print("1.3428 billion km is the distance from earth to saturn and it would take 23 months to reach there")


# Validating  Travel request in phase2       
if place == "Venus" or "venus" and namee == "mercury" or "Mercury":    
        print(" Earth is 115.36 million km away from mars and if you are traveling in 140,000 mph, it can take up to 6 and a half years to reach earth")

if place == "earth" or "earth" and namee == "mercury" or "Mercury":    
        print("earth is 76.15 million km away from venus and is you travel 12000mph, it can take 15 months to reach venus")        

if place == "Mars" or "mars" and namee == "mercury" or "Mercury":    
        print("106.35 million km is the distance from earth to mars and it would take roughly 8 months to reach your desired location depending on which spacecraft you are travelling with.")

if place == "Jupiter" or "jupiter" and namee == "mercury" or "Mercury":    
        print("620.25 million km is the distance from earth to jupiter and it would take 13 months to reach your desired location")

if place == "Uranus" or "uranus" and namee == "mercury" or "Mercury":    
        print("It would take around 3 to 4 yers to reach there because it 2.9895 billion km away from your home planet")
        
if place == "neptune" or "Neptune" and namee == "Mercury" or "mercury":    
        print("4.3826 billion km is the distance from earth of neptune and it would take 8 years to reach there ")
        
if place == "Saturn" or "saturn" and namee == "mercury" or "mercury":    
        print("1.3428 billion km is the distance from earth to saturn and it would take 23 months to reach there")
