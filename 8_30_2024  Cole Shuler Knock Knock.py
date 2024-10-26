#Cole Shuler, 8/29/2024
#This is a knock knock joke example with more than one final result

name = input('Hi! What is your name? ')
response = input(f'Hi {name}! Would you like to hear a joke? (Y/N) ')

if response.startswith('y') or response.startswith('Y'):
    print('Knock knock. ')
    response = input()#Who's there?
else:
    print("That stinks.")
    
if response == ("who's there?") or response == ("Who's there?"):
    print('Hoo... ')
    response = input()#Hoo who?
    
if response == ('hoo who?') or response == ('Hoo who?'):
    print('Why do you sound like an owl?')
    
else:
    print('Ok, bye bye!')

    

