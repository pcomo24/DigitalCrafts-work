unleet = input("enter a message ")
leetmsg = unleet
leetwords = "AEGIOSTaegiost"
for letter in unleet:
    if letter in leetwords:
        leetmsg = leetmsg.replace('a', '4')
        leetmsg = leetmsg.replace('A', '4')
        leetmsg = leetmsg.replace('e', '3')
        leetmsg = leetmsg.replace('E', '3')
        leetmsg = leetmsg.replace('G', '6')
        leetmsg = leetmsg.replace('g', '6')
        leetmsg = leetmsg.replace('i', '1')
        leetmsg = leetmsg.replace('I', '1')
        leetmsg = leetmsg.replace('o', '0')
        leetmsg = leetmsg.replace('O', '0')
        leetmsg = leetmsg.replace('s', '5')
        leetmsg = leetmsg.replace('S', '5')
        leetmsg = leetmsg.replace('t', '7')
        leetmsg = leetmsg.replace('T', '7')
print(leetmsg)
