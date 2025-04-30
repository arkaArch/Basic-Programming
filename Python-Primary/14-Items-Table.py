def print_table(items_dictionary, left_width, right_width):
    print()
    # Prints "ITEMS" with no of {(left_width + right_width)/2 - len(ITEMS)} '=' in left and right  
    print("ITEMS".center(left_width + right_width, '='))
    for k, v in items_dictionary.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width))
    print()

items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
print_table(items, 20, 6)

