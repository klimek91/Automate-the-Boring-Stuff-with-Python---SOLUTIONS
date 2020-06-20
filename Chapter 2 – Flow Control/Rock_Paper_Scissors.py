import random, sys
turns = 10
count = 0
wins = 0
losses = 0
ties = 0
print("ROCK, PAPER, SCISSORS: {} turns game".format(turns))

while count < turns:
    print("Turn no. {}: {} Wins, {} Losses {} Ties".format(count + 1, wins, losses, ties))
    print("Enter Your move: (r)ock, (p)aper, (s)cissors or (q)uit")
    guess = input()
    if guess.lower() == 'r' or guess.lower() == 'rock':
        guess = 'r'
        print('Rock versus..', end=' ')
        count += 1
    elif guess.lower() == 'p' or guess.lower() == 'paper':
        guess = 'p'
        print('Paper versus..', end=' ')
        count += 1
    elif guess.lower() == 's' or guess.lower() == 'scissors':
        guess = 's'
        print("Scissors versus..", end=' ')
        count += 1
    elif guess.lower() == 'q' or guess.lower() == 'quit':
        print('OK bye')
        sys.exit()
    else:
        print("You put incorrect input, try again")
        continue


    computer = random.choice(['Rock','Paper','Scissors'])
    print(computer)

    if guess == 'r':
        if computer == 'Rock':
            print('Its a TIE')
            ties+=1
        elif computer == 'Paper':
            print("You LOSE")
            losses+=1
        elif computer == 'Scissors':
            print("You WIN")
            wins+=1

    elif guess == 'p':
        if computer == 'Rock':
            print('You WIN')
            wins+=1
        elif computer == 'Paper':
            print("Its a TIE")
            ties+=1
        elif computer == 'Scissors':
            print("You LOSE")
            losses+=1

    if guess == 's':
        if computer == 'Rock':
            print('You LOSE')
            losses+=1
        elif computer == 'Paper':
            print("You WIN")
            wins+=1
        elif computer == 'Scissors':
            print("Its a TIE")
            ties+=1

print("FINAL RESULT: {} WINS, {} LOSSES, {} TIES".format(wins,losses,ties))