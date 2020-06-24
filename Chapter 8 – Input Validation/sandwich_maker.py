import pyinputplus as pyinp

total_cost = 0
bread = pyinp.inputMenu(['wheat','white','sourdough'])
if bread == 'wheat' or bread == 'sourdough':
    total_cost+=1.5
elif bread == 'white':
    total_cost+=1

protein = pyinp.inputMenu(['chicken','turkey','ham','tofu'])
if protein == 'chicken' or protein == 'ham':
    total_cost+=2
elif protein == 'turkey' or protein == 'tofu':
    total_cost+=2.5

cheese = pyinp.inputYesNo("Do You want cheese?")
if cheese == "yes":
    cheese_type = pyinp.inputMenu(['cheddar', 'Swiss', 'mozarella'])
    if cheese_type == 'cheddar' or cheese_type == 'mozarella':
        total_cost+=1
    elif cheese_type == 'Swiss':
        total_cost+=1.5
mayo = pyinp.inputYesNo("Do You want mayo?")
if mayo == 'yes':
    total_cost+=0.1
mustard = pyinp.inputYesNo("Do You want mustard?")
if mustard == 'yes':
    total_cost += 0.1
lettuce = pyinp.inputYesNo("Do You want lettuce?")
if lettuce == 'yes':
    total_cost += 0.1
tomato = pyinp.inputYesNo("Do You want tomato?")
if tomato == 'yes':
    total_cost += 0.1
amount = pyinp.inputInt("How many sandwiches  do You want?", min=1)
total_cost*=amount

print(round(total_cost, 2),'€')