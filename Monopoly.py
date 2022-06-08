import random
import csv
from os.path import exists as file_ex
import matplotlib.pyplot as plt

#Monoply board is represented by numbers with 0 being Go and 39 being Boardwalk
#Starting position for the game is on Go (0)
position = 0

#Array to store the number of times that tile has been landed on
tile = []
for i in range(40):
    tile.append(0)

#names of the properties
name1 = ["Go","Mediterranean Avenue", "Community Chest", "Baltic Avenue", "Income Tax", "Reading Railroad", "Oriental Avenue", "Chance", "Vermont Avenue", "Connecticut Avenue"]
name2 = ["Jail", "St. Charles Place", "Electric Company", "States Avenue", "Virginia Avenue", "Pennsylvania Railroad", "St. James Place", "Community Chest", "Tennessee Avenue", "New York Avenue"]
name3 = ["Free Parking", "Kentucky Avenue", "Chance", "Indiana Avenue", "Illinois Avenue", "B & O Railroad", "Atlantic Avenue", "Ventnor Avenue", "Water Works", "Marvin Gardens"]
name4 = ["Go to Jail","Pacific Avenue", "North Carolina Avenue", "Community Chest", "Pennsylvania Avenue", "Short Line", "Chance", "Park Place", "Luxury Tax", "Boardwalk"]
name = name1 + name2 + name3 + name4

if (file_ex('data.csv') == False):
    with open('data.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(name)

#Count how many doubles have been rolled
numDouble = 0

#How many dice rolls you want to simulate
numIter = int(input("Enter the number of dice roles to simulate: "))

for i in range(1, numIter + 1):
    #simulate dice rolls
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    dice = d1 + d2

    if (d1 == d2):
        numDouble = numDouble + 1
    else:
        numDouble = 0

    newPosition = position + dice
    if (newPosition > 39):
        position = newPosition - 40
    else:
        position = newPosition

    #simulating Chance cards
    if (position == 7 or position == 22 or position == 36):
        chanceCard = random.randint(1, 16)
        if (chanceCard == 1):
            #Advance to Boardwalk
            position = 39
        elif (chanceCard == 2):
            #Advance to Go
            position = 0
        elif (chanceCard == 3):
            #Advance to Illinois Ave
            position = 24
        elif (chanceCard == 4):
            #Advance to St. Charles Place
            position = 11
        elif (chanceCard == 5 or chanceCard == 6):
            #Advance to nearest railroad
            if (position == 7):
                position = 15
            elif (position == 22):
                position = 25
            elif (position == 36):
                position = 5
        elif (chanceCard == 7):
            #Advance to nearest Utility
            if (position == 7):
                position = 12
            elif (position == 22):
                position = 28
            elif (position == 36):
                position = 12
        elif (chanceCard == 10):
            #Go back 3 spaces
            position = position - 3
        elif (chanceCard == 11):
            #Go to Jail
            position = 10
        elif (chanceCard == 14):
            #Advance to Reading Railroad
            position = 5

    #simulating Comunity chest
    if (position == 2 or position == 17 or position == 33):
        communityCard = random.randint(1, 16)
        if (communityCard == 1):
            #Advance to Go
            position = 0
        elif (communityCard == 6):
            #Go to Jail
            position = 10

    #Go to jail square
    if (position == 30):
        position = 10

    #Go to jail if 3 doubles in a row
    if (numDouble == 3):
        position = 10
        numDouble = 0

    #Counting the number of times tile has been landed on
    tile[position] = tile[position] + 1

# Find the maximum length of number
maxLen = 0;
for x in range(1,41):
    tileNumber = x - 1
    toStr = str(tile[tileNumber])
    toStrLen = len(toStr)
    if (toStrLen > maxLen):
        maxLen = toStrLen

# Print the output
print("          Name         Count  Percent")
print("-" * 37)

with open('data.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(tile)

for x in range(1,41):
    tileNumber = x - 1
    space = ""
    for y in range (0, (21 - len(name[tileNumber]))):
        space += " "

    endSpace = "";
    for z in range (0, maxLen + 2 - len(str(tile[tileNumber]))):
        endSpace += " ";

    print(str(name[tileNumber])+ ": " + space + str(tile[tileNumber]) + endSpace, end='')
    print(" " + f"{round((tile[tileNumber] / numIter) * 100, 2): .2f}" + "%")
  
# x-coordinates of left sides of bars
left = []
for i in range (1, 41):
    left.append(i)
  
# heights of bars
percent = []

for i in tile:
    percent.append((i / numIter) * 100)

height = percent
  
# labels for bars
tick_label = name

color = ['black', 'brown', 'black', 'brown', 'black', ]
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.5, color = color)
  
# naming the x-axis
plt.xlabel('Name')
# naming the y-axis
plt.ylabel('# of times the turn ended')
# plot title
plt.title('Chance of ending a turn on each tile')

plt.xticks(rotation = 45)
# function to show the plot
plt.show()
