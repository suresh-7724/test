def temperature_matching(temp):
    if(temp>30):
        return "hot"
    elif(temp>=20 and temp<=30):
        return "Moderate"
    elif(temp<20):
        return "Cold"
    
temp=input("Enter the temperature: ")
print(temperature_matching(int(temp)))