catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()

    if name == '':
        break
    catNames = catNames + [name]

print('Your cats are: \n')
for cat in catNames:
    print(cat)

# Using range() in for-loops
supplies = ['pens', 'pencils', 'books', 'binders']

for item in range(len(supplies)):
    print('Index ' + str(item) + ' in supplies is: ' + supplies[item])

# Using 'in' in operations

greet = input(str('enter your greet keyword: ')).lower()

greetings = ['howdy', 'hello', 'hi', 'heyas']

if greet in greetings:
    print('your greet is present in the greetings list: ' + greet)
else:
    print('your greet : ' + greet + 'is not in the greeting list')

# Using 'not' in operations
myPets = ['kitty', 'sophie', 'brownie', 'holly', 'winter', 'summer']

your_pet = input(str('enter your pet name: '))

if your_pet not in myPets:
    print('you dont have a pet with this name: ' + your_pet)
else:
    print('you found your baby and its name is : ' + your_pet)
