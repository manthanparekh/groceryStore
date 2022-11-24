# TODO-1: Show inventory and prices  ------------------------- DONE
# TODO-2: repeat  asking user for inputs  until Done ---------
# TODO-3: end task when user inputs 'done --------------------
# TODO-4: print total items and cost when done ---------------
# TODO-5: use dictionary, functions, loops and conditionals --

# printing out welcome page with information
print("-----Welcome to the Ash's Grocery store!-----")
print("Please choose from the selected items below: ")

items = {
    'Bread' : 3.5,
    'Milk' : 2,
    'Cake' : 7,
    'Corona-Extra' : 10,
    'Coffee' : 15,
    'linux' : 0
}
print(items)
inventory = ["bread", "milk", "cake", "corona", "coffee", "linux"]
print(inventory)
print("Which items would you like? ")
print("when finished type 'done'")

# creating an empty cart of items and then adding in
cart = []
def item_to_cart(item):
    cart.append(item)


while True:
    new_item = input("Add an item: ")

    if new_item == 'done':
        break