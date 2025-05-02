# Here we take an example of American phone number like: 415-555-9807

def is_phone_number(text):
    # The length of phone number must be 12
    if len(text) != 12:
        return False
    # 4th and 8th character must be a '-'
    if text[3] != '-' and text[7] != '-':
        return False
    # From 1st to 3rd character must be number
    for i in range(3):
        if not text[i].isdecimal():
            return False
    # From 5th to 7th character must be number
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False   
    # From 1st to 3rd character must be number
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me at 415-555-2022 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print(chunk)
