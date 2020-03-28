kilo_pascal = float(input("Enter the number of kilo pascals :"))
pounds = 0.15*kilo_pascal
milli_m_of_Hg = 7.50*kilo_pascal
atmos = kilo_pascal*0.0099
print("The equivalent pressure in pounds per square inch is :%f\nThe equivalent pressure in millimeters of mercury is %f\nThe equivalent pressure in atmospheres is %f")%(pounds,milli_m_of_Hg,atmos)
