def display_inventory():
    inventory = list(inv)
    number_of_items = list(inv.values())
    print('Inventory:\n')
    for i in inventory:
        print(i, '\n')
    for j in number_of_items:
        print(j, '\n')
    print('Total number of items: ', sum(number_of_items))   




def add_to_inventory(inv, dragon_loot):
    added_items = [['gold coin', dragon_loot.count('gold coin') + inv['gold coin']],
                ['dagger', dragon_loot.count('dagger') + inv['dagger']],
                ['ruby', dragon_loot.count('ruby')],
                ['rope', dragon_loot.count('rope') + inv['rope']],
                ['torch', dragon_loot.count('torch') + inv['torch']],
                ['arrow', dragon_loot.count('arrow') + inv['arrow']]
    ]
    inv_clone = dict(added_items)
    inv.update(inv_clone)

    display_inventory()

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

add_to_inventory(inv, dragon_loot)