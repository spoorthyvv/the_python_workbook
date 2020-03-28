foot = int(input("Enter your height in feet>>> :"))
inches = int(input("Enter the height .(after the decimal point) inches >>>:"))
height_in_inches = foot*12
height_in_centimeters = height_in_inches*2.54
height_in_centimeters2 = inches*2.54
print("Your height in centimeters is :",(height_in_centimeters+height_in_centimeters2))
