#Sum/Average Program
#Your First and Last Name: Veronica Marquez
#Your Student ID: s1125739

tot = 0
numberList = []

for x in range(0,20):
    num = int(input('Enter a number'))
    numberList.append(num)
for x in range(0,20):
    tot = tot + numberList[x]

print('The sum of the number you entered is:' , tot)
print('The average of the numbers you entered is:' , tot/len(numberList))
