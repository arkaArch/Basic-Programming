import re

message = 'Call me at 435-786-9086 tomorrow.'

phone_number_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
# phone_number_regex contains a regex object
try:
    matching_object = phone_number_regex.search(message)
    # If it not finds any pattern matching with regex object, matching_object returns 'None'
    # And if we try to access group() in None type object it gives us AttributeError.
    print(matching_object.group())
except AttributeError:
    print("No phone number found")


another_msg = 'Call me at 415-555-2022 tomorrow. 415-555-9999 is my office.'
phone_numbers = phone_number_regex.findall(another_msg)
for phone_number in phone_numbers:
    print(phone_number)
