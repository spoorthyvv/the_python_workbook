number_1 = int(input("Enter the first number :"))
number_2 = int(input("Enter the second number :"))
number_3 = int(input("Enter the third number :"))

s1 = min(number_1,number_2,number_3)
l1 = max(number_1,number_2,number_3)
m1 =(number_1+number_2+number_3)-l1-s1

print("The numbers are sorted from smallest to largest:%d :%d :%d"%(s1,m1,l1))

