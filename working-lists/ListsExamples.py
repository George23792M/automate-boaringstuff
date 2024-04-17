

print('list range 0 - 100 = ' + str(list(range(0, 100, 2))))


office_supplies = ['books', 'pens', 'pencils', 'staplers', 'tape', 'papers', 'daily-planners']

# for loop using len() of array and range() to
# print index of the item and office supply item

for item in range(len(office_supplies)):
    print('Index ' + str(item) + ' in supplies is: ' + office_supplies[item])


# python has a multi assign variables:
cat = ['fat', 'orange', 'kitty']

# multiple assignment variables 
size, color, name = cat

print('size of a cat ' + str(size).upper() + ' and color of a cat is ' + str(color).upper() + ' and name of the cat is ' + str(name).upper())

