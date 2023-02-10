# IF Else

print("Enter your marks")
numbers = int(input())
print(numbers)

# if 90 < numbers < 100:
if numbers < 90 or numbers < 100:
    grade = 'A'
elif 80 < numbers < 100:
    grade = 'B'
else:
    grade = 'Dont know'
print("The grade is ", grade)