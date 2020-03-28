number = int(input("Enter the number :"))
sum = 0
while(number!=0):
	sum = sum +int(number%10)
	number = int(number/10)
print("The sum of the digits is :",sum)
