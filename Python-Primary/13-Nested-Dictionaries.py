all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}


print('Apples brought by Alice: %s\n' % all_guests['Alice']['apples'])

# Calculate total number of items brought by all guests
def total_brought(guests, item):
    item_brought = 0
     
    # If item is brought increase number of items, else add 0
    """ Longer code:

    for k, v in guests.items():
        if item in v:
            item_brought += v[item]
    """
    for k, v in guests.items():
        item_brought += v.get(item, 0)

    return item_brought

print('Number of things being brought:')
print(' - Apples         ' + str(total_brought(all_guests, 'apples')))
print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes          ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))
