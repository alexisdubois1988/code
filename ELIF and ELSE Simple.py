print('Hello!')
print('Please type your age.')
myage=input()
if int(myage) < 20:
    print('No access kiddo')
elif int(myage) < 40:
    print('That\'s more like it')
elif int(myage) < 60:
    print('That\'s a bit old')
elif int(myage) < 80:
    print('No way!')
else:
    print('Are you dead?')