# Finds phone number and email address on the clipboard
import re, pyperclip

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?         # area code is optional(?)
    (\s|-|_|\.)?               # separator(space, -, _, .)         
    (\d{3})                    # first three digits
    (\s|-|_|\.)?               # separator(space, -, _, .)         
    (\d{4})                    # last four digits
    )''', re.VERBOSE)
# re.VERBOSE as a second argument in re.compile() use to ignore whitespaces and comments
# inside of re.compile()
# ? 94010-4093 this can be treated as phone number and print: -010-4093

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+          # username(make a character class with all possible combination)
    @                          # at the rate of
    [a-zA-Z0-9.-]+             # domain name(again with character class)
    (\.[a-zA-Z]{2,4})          # .top_lvl_domain with 2 to 4 character
    )''', re.VERBOSE)

# Find matches in clipboard text:
text = str(pyperclip.paste())

matches = []

for groups in phone_regex.findall(text):
    # Format various phone number into a certain format
    phone_number = '-'.join([groups[1], groups[3], groups[5]])
    # groups[2] and groups[4] contain space/-/_/.
    matches.append(phone_number)

for groups in email_regex.findall(text):
    matches.append(groups[0])


# Print result:
if len(matches) > 0:
    print("Email and Phone numbers are...")
    print('\n'.join(matches))
else:
    print("No phone numbers and email addresses found")


# Open the url 'https://nostarch.com/contactus', copy all with CTRL+A in clipboard
# Then run the program
