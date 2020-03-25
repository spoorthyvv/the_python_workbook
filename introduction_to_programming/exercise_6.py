meal_cost = float(input("Please Enter the cost of Your meal ::"))
tip_generated = ((meal_cost*18)/100)
tax_generated = ((meal_cost*5)/100)
#assuming that the tax of the meal is 5% as per the hotel
total_bill = meal_cost+tip_generated+tax_generated
print("Thank you.Your bill is :",total_bill,"/-")
