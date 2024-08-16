inventory = [('Book', 10), ('Pen', 0), ('Pencil', 5), ('Eraser', 7), ('Scale', 3)]

def check_inventory(inventory):
    for x, y in inventory:
        if y <= 0:
            print(x + " is out of stock!")

check_inventory(inventory)