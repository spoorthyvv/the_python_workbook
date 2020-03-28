seconds = float(input("Enter the total number of seconds >>> :"))
days = seconds/(24*60*60)
seconds = seconds%(24*60*60)
hours = (seconds/(60*60))
seconds = (seconds%(60*60))
minutes = seconds/60
seconds = seconds%60
seconds_left = seconds
print("The format in D:HH:MM:SS is : %d:%d:%d:%d"%(days,hours,minutes,seconds_left))

