#Sum/Average Program
#Your First and Last Name: Veronica Marquez
#Your Student ID: s1125739

list = []
for i in range(0,20):
    numbers = int(input("enter number: "))
    list.append(numbers)
print('The sum of the number you entered is:' , sum(list))
print('The average of the numbers you entered is:' , (sum(list)/len(list)))

