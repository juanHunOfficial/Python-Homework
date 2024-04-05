#Author: Hun, Juan P.


number_of_iterations = int(input("Enter the number of iterations for the loop: "))

denominator = 1
sum = 0
#doing 4 divided by the denominator gets the same result as dividing the sum by 4 at the end
#the way the book has the formulate laid out.
for current_value in range(number_of_iterations):
    if current_value % 2 == 0:
        sum += 4/denominator
    elif current_value % 2 != 0:
        sum -= 4/denominator

    denominator += 2

print(sum)