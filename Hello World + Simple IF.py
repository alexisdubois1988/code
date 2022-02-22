#This program says hello and ask for my name

print('Hello world!')
input() # blank
print('What is your name?')
myname=input()
print('Happy to meet you, '+ myname +'.')
print('The lenght of your name is:')
print(len(myname))
print('What is your age?')
myage=input()
print('That means you will be ' + str(int(myage)+1) + ' in a year.')
input()
if(int(myage))<30:
    print('You are very young!')
elif(int(myage))<60:
    print('You are still ok!')
else:
    print('You are experienced!')