bill = int(input("Total bill amount?"))
service = input("Level of service?(good,fair, bad)")
people_amt = int(input("Split how many ways?"))
if service == "good":
    tip = .2 * bill
    print("Tip amount: $" + str(tip))
    print("Total bill: $" + str(bill + tip))
    print("Amount per head: $" + str((bill + tip) / people_amt))
elif service == "fair":
    tip = .15 * bill
    print("Tip amount: $" + str(tip))
    print("Total bill: $" + str(bill + tip))
    print("Amount per head: $" + str((bill + tip) / people_amt))
else:
    print("Tip amount: $" + str(tip))
    print("Total bill: $" + str(bill + tip))
    print("Amount per head: $" + str((bill + tip) / people_amt))
