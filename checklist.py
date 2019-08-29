# Captain Rainbox's Color Checklist: https://www.makeschool.com/academy/track/captain-rainbow-s-color-checklist

# Create our Checklist
checklist = list()

# Define Functions
# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# Mark Complete
def mark_completed(index):
    update(index, "√ " + checklist[index])
    print("Marked " + checklist[index] + ". Updated Checklist:")
    list_all_items()

# Select
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number? ")

        # Remember that item_index must actually exist or our program will crash.
        print(read(int(item_index)))

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Quit
    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

# TEST
def test():
    create("purple sox")
    #create("red cloak")

    #print(read(0))
    #print(read(1))

    update(0, "Purple Socks")
    #destroy(1)

    #print(read(0))
    create("Yellow Shoes")
    create("Green Watch")
    create("Orange Shirt")
    list_all_items()

    mark_completed(1)

    # # Call your new function with the appropriate value
    # select("C")
    # # View the results
    # list_all_items()
    # # Call function with new value
    # select("R")
    # # View results
    # list_all_items()
    # # Continue until all code is run

# Run Tests
test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit ")
    running = select(selection)