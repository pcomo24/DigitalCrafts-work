day = int(input('Day (0-6)? '))
#print({day}).format("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
if day == 0 or 6:
    print("Sleep in")
else:
    print("Go to work")
