# Loops

"""
#For Loops
print('How many times do you want to execute')
no = int(input())
for i in range(0, no):
    print(i)

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for item in list1:
    for i in item:
        print(i)
"""

# While Loops
print("Enter a number")
numbers = int(input())
while numbers > 4:
    print("Numer is greater than 4")
    numbers = int(input())
    if numbers == 9:
        break
    if numbers == 8:
        continue
    print('Loop ended')
