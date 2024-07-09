number_of_eggs_entered = int(input("Enter the number of eggs you need seperated:"))

DOZEN_EGGS = 12

results = number_of_eggs_entered // DOZEN_EGGS
singles = number_of_eggs_entered % DOZEN_EGGS

print("You have : ", results, " dozen of eggs, and: ", singles, " is your remainder.")