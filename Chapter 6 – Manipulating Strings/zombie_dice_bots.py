import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        shotgun= 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']

            if shotgun <2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class RollAndRandom(MyZombie):
    def turn(self, gameState):
        diceRollResult = zombiedice.roll()
        while diceRollResult is not None:
            guess = random.randint(0,1)
            if guess == 1:
                diceRollResult = zombiedice.roll()
            else:
                break

class Stop2brain(MyZombie):
    def turn(self, gameState):
        diceRollResult = zombiedice.roll()
        brain = 0
        while diceRollResult is not None:
            brain+= diceRollResult['brains']
            if brain != 2:
                diceRollResult = zombiedice.roll()
            else:
                break

class Stop2guns(MyZombie):
    def turn(self, gameState):
        diceRollResult = zombiedice.roll()
        shotgun = 0
        while diceRollResult is not None:
            shotgun+= diceRollResult['shotgun']
            if shotgun != 2:
                diceRollResult = zombiedice.roll()
            else:
                break

class OneToFour(MyZombie):
    def turn(self, gameState):
        diceRollResult = zombiedice.roll()
        shotgun = 0
        count = 1
        while diceRollResult is not None:
            shotgun+= diceRollResult['shotgun']
            while count <5:
                if shotgun == 2:
                    break
                diceRollResult = zombiedice.roll()
                count+=1
            break

class MoreGunsThenBrain(MyZombie):
    def turn(self, gameState):
        diceRollResult = zombiedice.roll()
        shotgun = 0
        brains = 0
        while diceRollResult is not None:
            shotgun+= diceRollResult['shotgun']
            brains += diceRollResult['brains']
            if shotgun > brains:
                break
            else:
                diceRollResult = zombiedice.roll()


zombies = (#zombiedice.examples.RandomCoinFlipZombie(name='Random'),\
           #zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),\
           #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2Shotguns', minShotguns=2),\
           #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1Shotgun', minShotguns=1),\
           MyZombie(name='My Zombie Bot'),\
           RollAndRandom(name="Roll and Random"),\
           Stop2brain(name="Stop when 2 brains"),\
           Stop2guns(name="Stop when 2 shotguns"),\
           OneToFour(name="1-4 rolls or 2 shotguns"),\
    MoreGunsThenBrain(name="MoreGunsThenBrain")
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)