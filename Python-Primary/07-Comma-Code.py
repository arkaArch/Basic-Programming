def list_to_string(list_value):
    string_value = ''
    i = 0
    for i in range(len(list_value) - 1):
        string_value += list_value[i] + ', '
    # Delete trailing ' ' and ',', then concat
    return string_value[:-2] + ' and ' + list_value[i+1] + '.'


spam = ['apples', 'bananas', 'tofu', 'cats', 'bat', 'rat']
print(list_to_string(spam))
    
