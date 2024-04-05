#Author: Hun, Juan P.

list_of_numbers = input("Enter a list of integers to calculate the sum: ")
list_of_numbers = list_of_numbers.split(",")

sum = 0
count = 0
while count < len(list_of_numbers):
    sum += int(list_of_numbers[count])
    count += 1


average = sum / len(list_of_numbers)
print(f"The sum is {sum} and the average is {average}")