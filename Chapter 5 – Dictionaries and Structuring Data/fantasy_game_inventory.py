eq = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory")
    sum = 0
    for k,v in inventory.items():
        sum+=v
        print(v, k)
    print("Total number of items: {}".format(sum))

displayInventory(eq)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'sword', 'gold coin', 'gold coin', 'gold coin']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item]+=1
        else:
            inventory.setdefault(item, 1)

addToInventory(eq, dragonLoot)
displayInventory(eq)