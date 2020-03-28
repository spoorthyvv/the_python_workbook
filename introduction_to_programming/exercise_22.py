length_of_side_1 = float(input("Enter the length of the first side of the triangle >> :"))
length_of_side_2 = float(input("Enter the length of the second side of the triangle >> :"))
length_of_side_3 = float(input("Enter the length of the third side of the triangle >> :"))
s1 = length_of_side_1
s2 = length_of_side_2
s3 = length_of_side_3
s = (s1+s2+s3)/2
area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
print("The area of the triangle is>> :",area,"m^2")

