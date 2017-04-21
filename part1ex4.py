day = int(input('Day (0-6)? '))
#print({day}).format("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
if day == 0:
    print("Sunday")
elif day == 2:
    print("Tuesday")
elif day == 3:
   print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print ("Friday")
else:
    print("Saturday")
