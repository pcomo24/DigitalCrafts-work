bill = int(input("Total bill amount?"))
service = input("Level of service?(good,fair, bad)")
#tip = ""
if service == "good":
    tip = .2 * bill
    print("Tip amount: $" + str(tip))
    print("Total bill: $" + str(bill + tip))
elif service == "fair":
    tip = .15 * bill
    print("Tip amount: $" + str(tip))
    print("Total bill: $" + str(bill + tip))
else:
    print("Tip amount: $" + str(tip))
    print("Total bill: $" + str(bill + tip))
