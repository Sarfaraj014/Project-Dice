# Game Description
# I have developed a simple game that allows users to play Ludo without a physical dice by using 
# a computer-generated dice system.

# The player only needs to enter a dice number, and the computer will automatically generate 
# random dice points.
# To exit the game, type 0 and press Enter.
import random
import os
dicelist= ('''
        ┌─────────┐
        │  ●      │
        │         │
        │      ●  │
        └─────────┘''',
        '''
        ┌─────────┐
        │  ●      │
        │         │
        │      ●  │
        └─────────┘''',
        '''
        ┌─────────┐
        │  ●      │
        │    ●    │
        │      ●  │
        └─────────┘''',
        '''
        ┌─────────┐
        │  ●   ●  │
        │         │
        │  ●   ●  │
        └─────────┘''',
        '''
        ┌─────────┐
        │  ●   ●  │ 
        │    ●    │ 
        │  ●   ●  │ 
        └─────────┘ ''',
        '''
         ┌─────────┐ 
         │  ●   ●  │ 
         │  ●   ●  │ 
         │  ●   ●  │ 
         └─────────┘ 
''')
while True:
    userinput=input("How many dice do you want : ")
    os.system("clear")
    if int(userinput) == 0:
        break
    for i in range(0,int(userinput)):
        print(random.choice(dicelist))
    