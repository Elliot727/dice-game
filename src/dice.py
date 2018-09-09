import random

# start loop
loop = 0

total = 0
total2 = 0

while loop < 5:
    print("LOOP = " + str(loop))
    print("      ")
    print("player 1")
    dice = random.randint(1,6)
    print("The dice value is: " + str(dice))
    dice2 = random.randint(1,6)
    print("The dice2 value is: " + str(dice2))
    print("player 2")
    dice3 = random.randint(1,6)
    print("The dice value is: " + str(dice3))
    dice4 = random.randint(1,6)
    print("The dice2 value is: " + str(dice4))

    # The points rolled on each player’s dice are added to their score.

    total = total +  dice + dice2
    print("player 1 = " + str(total))
    total2 = total2 + dice3 + dice4
    print("player 2 = " + str(total2))

    # If the total is an even number, an additional 10 points are added to their score.
    # If the total is an odd number, 5 points are subtracted from their score.

    # player 1

    if (total % 2) == 0:
        total = total + 10
    else:
        total = total -5

    print("player 1 = " + str(total))

    # player 2

    if (total2 % 2) == 0:
        total2 = total2 + 10
    else:
        total2 = total2 -5

    print("player 2 = " + str(total2))

    # If they roll a double, they get to roll one extra die and get the number of points rolled added to their score.

    if dice == dice2:
        extradice1 = random.randint(1,6)
        print("extradice1 = "+ str(extradice1))
        total = total + extradice1

    print("player 1 extradice = " + str(total))

    if dice3 == dice4:
        extradice2 = random.randint(1,6)
        print("extradice2 = "+ str(extradice2))
        total2 = total2 + extradice2

    print("player 2 extradice = " + str(total2))    

    # The score of a player cannot go below 0 at any point.

    if total <0:
        total = 0

    if total2 <0:
        total2 = 0

    print("PLAYER 1 FINAL SCORE = " + str(total))
    print("PLAYER 2 FINAL SCORE = " + str(total2))
    
    loop = loop + 1

# The person with the highest score at the end of the 5 rounds wins.
# If both players have the same score at the end of the 5 rounds, they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins).


