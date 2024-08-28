#S Krishna
#Assignment 2
# Use of IF statements with AND/OR operators.

Grade = int(input(“What grade are you in? (1-12)”))

if(Grade<1 or Grade>12):
    print(“Sorry. Only 1-12 allowed. Rerun the program!”)

if(Grade>=1 and Grade<=5):
    print(“You are in Elementary!”)

if(Grade>=6 and Grade<=8):
    print(“You are in Middle School!”)

if(Grade>=9 and Grade<=12):
    print(“You are in High School!”)
    if (Grade == 10):
        print(“Good luck with the IGCSE if you are taking it!”)
    if (Grade == 12):
		print(“Good luck with the IB if you are doing the diploma!”)

