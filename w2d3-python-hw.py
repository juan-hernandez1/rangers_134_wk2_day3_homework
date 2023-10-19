# Exercise 1) 
# Build a Shopping Cart
# You can use either lists or dictionaries. 
# The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list


cart =  {}

while True:

    response = input("What would you like to do? add/delete/view/quit: ")

    if response == "add":
        new_item = input("What would you like to add? ")
        cart[new_item] = cart.get(new_item, 0) + 1
        print(f"{new_item} has been added to your cart. ")
    elif response == "delete":
        takeout = input("What would you like to remove? ")
        if takeout in cart and cart[takeout] > 0:
            cart[takeout] -= 1
            print(f"{takeout} has been removed from your cart.")
        else:
            print(f"{takeout} is not in your cart.")
    elif response == "view":
            print("This is what is in your cart:")
            for item in cart.items():
                print(f"{item}")
    elif response == "quit":
        break
    else:
        print("Invalid input. Please choose add, delete, view, or quit.")
        
print("This is what is in your cart:")
for item in cart.items():
    print(f"{item}")

# 2) Set Practice
# Remove all duplicates from the following list

nums_list = [1, 1, 1, 2, 2, 3, 5, 6, 4, 12, 11, 12, 12, 14, 16, 16, 16, 1, 1, 1, 2, 2]

remove_dups = set(nums_list)
print(remove_dups)

nums_list = list(remove_dups)

print(nums_list)

# Out put the intersection of the following the following sets.
set1 = {20, 24, 26, 27}
set2 = {26, 35, 63, 27}

set3 = set1.intersection(set2)
print(set3)

#Output the difference between the following sets
set3 = {100, 65, 89, 200}
set4 = {65, 103, 54, 200}

set5 = set3.difference(set4)
print(set5)