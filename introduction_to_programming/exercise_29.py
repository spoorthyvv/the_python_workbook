import math
math.floor


air_temp = int(input("Enter the air temperature in degree celsius :"))
wind_speed = int(input("Enter the wind speed in miles per hour :"))
wci =13.12+(0.6215*air_temp)-(11.37*(wind_speed**0.16))+(0.3965*air_temp*(wind_speed**0.16))
print("The wind chill index is:",math.floor(wci))
