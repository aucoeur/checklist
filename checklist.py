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
    print("Marked" + checklist[index] + ". Updated Checklist:")
    list_all_items()

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

test()