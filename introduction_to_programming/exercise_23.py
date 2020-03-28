import math
math.tan



#let s be the length of the polygon
s = float(input("Enter the length of the polygon >>> :"))


#let n be the no of sides of the polygon
n = float(input("Enter the number of sides of the polygon >>:"))

area_of_the_polygon = ((n*(s**2))/4*(math.tan(180/n)))
print("The area of the polygon is >>> :",area_of_the_polygon,"m^2")

