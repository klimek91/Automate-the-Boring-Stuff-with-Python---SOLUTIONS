spam = ['apples', 'bananas', 'tofu', 'cats']

string = ''

string = ', '.join(spam[0:-1]) + ' and ' + spam[-1] + '.'


#or II solution

string2 = ''

for i in range(len(spam)):
    if i == len(spam)-2:
        string2 += spam[i] + ' and '
    elif i == len(spam) -1:
        string2 += spam[i] + '.'
    else:
        string2 += spam[i] + ', '
