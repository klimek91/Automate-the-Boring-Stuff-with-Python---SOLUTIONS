import pyinputplus as pyip

#1. Ask the user if they’d like to know how to keep an idiot busy for hours.
#2. If the user answers no, quit.
#3. If the user answers yes, go to Step 1.

while True:
    answer = pyip.inputYesNo("Would You like to know how to keep an idiot busy for hours? ")
    if answer == "no":
        print("OK, bye")
        break
    else:
        continue