import random

list = []
for i in range(10000):
    list.append(random.choice(['T', 'H']))

count = 0
for i in range(len(list)-5):
    #print(list[i:i+6])
    if list[i] == list[i+1] == list[i+2] == list[i+3] == list[i+4] == list[i+5]:
        count +=1

print("There were {} streaks of six heads or six tails in a row".format(count))