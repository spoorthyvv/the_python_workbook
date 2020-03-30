years = float(input("Enter the relevant human years :"))
if years<0:
	print("The entered number is a negative number. Enter an appropriate number")
elif years==1:

	print("The age with respect to dog years is :",(10.5/2)*years+"years")
else:
	print("The age with respect to dog years is :",((10.5)+4*(years-2)),"years")
