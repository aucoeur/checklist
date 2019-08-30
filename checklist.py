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

# Check if index is valid
def check_input(input):
    if int(input) >= len(checklist):
        print("Invalid Index.  Please try again. ")
        return True
    else:
        return False


# Select
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        invalid = True
        while invalid:
            index = user_input("Index Number? ")
            invalid = check_input(index)
        # Remember that item_index must actually exist or our program will crash.
        print("Item: " + read(int(index)))
    
    elif function_code == "U":
        list_all_items()

        invalid = True
        while invalid:
            index = user_input("Update which item? (Select index) ")
            invalid = check_input(index)

        item = user_input("Change to: ")
        update(int(index), item)
        print("Item changed. Updated List below:")
        list_all_items()
    
    elif function_code == "D":
        list_all_items()

        invalid = True
        while invalid:
            index = user_input("Delete which item? (Select index) ")
            invalid = check_input(index)

        destroy(int(index))
        print("Item deleted.  Updated List below: ")
        list_all_items()

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

    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run
    select("U")
    # Call function with new value
    select("D")

# Run Tests
test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, U to update item, D to delete item, and Q to quit ")
    running = select(selection.upper())