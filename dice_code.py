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
    userinput=input("how many dice do you want")
    os.system("clear")
    if int(userinput) == 0:
        break
    for i in range(0,int(userinput)):
        print(random.choice(dicelist))
    