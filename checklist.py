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

# def list_all_items():
#     index = 0
#     for list_item in checklist:
#         print(str(index) + list_item)
#         index += 1

# TEST
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1)) 

test()
