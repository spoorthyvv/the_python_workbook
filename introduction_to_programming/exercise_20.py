#SCUBA tank contains 20,000,000 pascals of pressure having volume of 12 litre's at 20 degree as the temperature 
#R is the universal gas constant having the value 8.314joule/mole K
pressure = float(input("Please enter the pressure of the gas in pascals >>> :"))
volume = float(input("Please enter the volume of the gas in litres >>> :"))
gas_constant = 8.314
temp_in_degree = float(input("Please enter the temperature of the gas in Degrees >>> :"))
temp_in_kelvin = temp_in_degree + 273.15
no_of_moles = (pressure*volume)/(gas_constant*temp_in_kelvin)
print("The number of moles of the  gas is equal to >>> :",no_of_moles)

