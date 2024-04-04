NEW_VIDEO_PRICE = 3.00
OLDIES_VIDEO_PRICE = 2.00

nights_rented = int(input("Enter in how long you want to rent for: "))
quantity_of_oldies = int(input("Enter the number of oldies: "))
quantity_of_new = int(input("Enter the number of new videos: "))

total_cost = nights_rented * ((quantity_of_new * NEW_VIDEO_PRICE) +
              (quantity_of_oldies * OLDIES_VIDEO_PRICE))

print("Your total today is: ", total_cost)
