# Pig Latin:
'''
If a word begins with a vowel, the word yay is added to the end of it.
If a word begins with a consonant or consonant cluster (like ch or gr), 
that consonant or cluster is moved to the end of the word followed by ay.
'''

print('Enter the English message to translate into Pig Latin: ')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u')
pig_latin = []

for word in message.split():
    # We want 'Hello!' => 'Ellohay!' not 'Ello!hay'
    # Scan each word's first and last letter.
    # If there is a non-alpha value at start or last store this into a variable.
    # And make the word free of non-alpha value
    
    # Separate the non-letters at the start of the word.
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        # Remove the first letter form string
        # Thus if, word = '@arka', then prefix_non_letter = '@' and word = 'arka'     
        word = word[1:]
    
    # Above loop is over when the len(word) = 0
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    # Separate the non-letters at the end of the word.
    suffix_non_letters = ''
    while not word[-1].isalpha():
        # Thus if, word = 'Hello!', then suffix_non_letter = '!' and word = 'Hello'     
        suffix_non_letters += word[-1]
        word = word[:-1]

    # Remember whether the word is in uppercase or titlecase
    was_upper = word.isupper()
    was_title = word.istitle()

    # Make the word lowercase for translation
    word = word.lower()

    # Now separate consonant or consonant cluster at the start of the word
    prefix_consnant = ''
    while len(word) > 0 and word[0] not in VOWELS:
        prefix_consnant += word[0]
        word = word[1:]
    
    # Add the Pig Latin ending to the word:
    # If word starts with consonant
    if prefix_consnant != '':
        word += prefix_consnant + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # Append the word in the pig_latin:
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)


# Join all the words back together into a single string:
print(' '.join(pig_latin))
