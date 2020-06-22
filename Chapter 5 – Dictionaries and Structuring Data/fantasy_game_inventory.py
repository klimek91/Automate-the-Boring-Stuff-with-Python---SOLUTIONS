eq = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory")
    sum = 0
    for k,v in inventory.items():
        sum+=v
        print(v, k)
    print("Total number of items: {}".format(sum))

displayInventory(eq)