#write a program to find the largest number in the list

numbers = [3, 6, 2, 10, 8, 4]
max = numbers[0]
for number in numbers:
    if number>max:
        max = number
print(max)