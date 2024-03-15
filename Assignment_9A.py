
# Assignment 9 / Problems 1 - 15

import re

# Problem 1 
text = ["ABCDEFabcdef123450", "*&%@#!}{"]
pattern = re.compile(r'[a-zA-Z0-9]+') 

print("Problem 1:\ncheck that a string contains only a certain set of "
"characters (in this case a-z, A-Z and 0-9).\n")
for t in text:
    matches = pattern.finditer(t)
    print(f"Text: {t}")
    found_match = False
    for match in matches:
        print(match)
        found_match = True
    if not found_match:
        print("No match")
    print()

# Problem 2
text = ["ab", "abc", "a", "ab", "abb"]
pattern = re.compile(r'ab*')

print("Problem 2:\nmatches a string that has an a followed by zero or more b's.\n")
for t in text:
    matches = pattern.finditer(t)
    print(f"Text to check: {t}")
    found_match = False
    for match in matches:
        print(match)
        found_match = True
    if not found_match:
        print("No match")
    print()

# Problem 3
text = ["ab", "abc", "a", "ab", "abb"]
pattern = re.compile(r'ab+')

print("Problem 3:\nmatches a string that has an a followed by one or more b's.\n")
for t in text:
    matches = pattern.finditer(t)
    print(f"Text to check: {t}")
    found_match = False
    for match in matches:
        print(match)
        found_match = True
    if not found_match:
        print("No match")
    print()

# Problem 4

text = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]
pattern = re.compile(r'\b[a-z]+_[a-z]+\b')

print("Problem 4:\nFind sequences of lowercase letters joined by an underscore.\n")
for t in text:
    matches = pattern.finditer(t)
    print(f"Text to check: {t}")
    found_match = False
    for match in matches:
        print(match)
        found_match = True
    if not found_match:
        print("No match")
    print()

# Problem 5
text = ["The quick brown fox jumps over the lazy dog.", " The quick brown fox jumps over the lazy dog."]
pattern = re.compile(r'\b\w+')

print("Problem 5:\nMatches a word at the beginning of a string.\n")
for t in text:
    matches = pattern.finditer(t)
    print(f"Text to check: {t}")
    found_match = False
    for match in matches:
        print(match)
        found_match = True
    if not found_match:
        print("No match")
    print()

# Problem 6
text = ["The quick brown fox jumps over the lazy dog.", "Python Exercises."]
pattern = re.compile(r'\b\w*z\w*\b')

print("Problem 6:\nMatches a word containing 'z'.\n")
for t in text:
    matches = pattern.finditer(t)
    print(f"Text to check: {t}")
    found_match = False
    for match in matches:
        print(match)
        found_match = True
    if not found_match:
        print("No match")
    print()

# Problem 7
ip = "216.08.094.196"
pattern = re.compile(r'\b0*(\d+)\b')

print("Problem 7:\nRemove leading zeros from an IP address.\n")
matches = pattern.finditer(ip)
for match in matches:
    print(match.group(1))
print()

# Problem 8
text = 'The quick brown fox jumps over the lazy dog.'
words = ['fox', 'dog', 'horse']

print("Problem 8:\nSearch for literal strings within a string.\n")
for word in words:
    pattern = re.compile(re.escape(word))
    matches = pattern.finditer(text)
    print(text)
    print(f"Word to search: {word}")
    found_match = False
    for match in matches:
        print(match)
        found_match = True
    if not found_match:
        print("No match")
print()

# Problem 9
text = 'The quick brown fox jumps over the lazy dog.'
word = 'fox'

print("Problem 9:\nSearch for a literal string in a string and find its location.\n")
pattern = re.compile(word)
matches = pattern.finditer(text)
found_match = False
for match in matches:
    print(text)
    print(f"Word to search: {word}\nLocation: {match.start()}-{match.end()}")
    found_match = True
if not found_match:
    print("No match")
print()

# Problem 10
text1 = "Regular Expressions"
text2 = "Code_Examples"

print("Problem 10:\nReplace whitespaces with an underscore and vice versa.\n")

modified_text1 = text1.replace(' ', '_')
print(f"Original Text: {text1}")
print(f"Modified Text: {modified_text1}\n")
modified_text2 = text2.replace('_', ' ')
print(f"Original Text: {text2}")
print(f"Modified Text: {modified_text2}\n")

# Problem 11
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
pattern = re.compile(r'(\d{4})/(\d{2})/(\d{2})')

print("Problem 11:\nExtract year, month, and date from a URL.\n")
match = pattern.search(url)
print(f"url = {url}")
if match:
    print(f"Year: {match.group(1)}")
    print(f"Month: {match.group(2)}")
    print(f"Day: {match.group(3)}")
else:
    print("No match")
print()

# Problem 12
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
pattern = re.compile(r'\b[a|e]\w+')

print("Problem 12:\nFind all words starting with 'a' or 'e' in a given string.\n")
print(f"Text to check: {text}\n ")
matches = pattern.finditer(text)
found_match = False
for match in matches:
    print(match)
    found_match = True
if not found_match:
    print("No match")
print()

# Problem 13
text = 'Python Exercises, PHP exercises.'
pattern = re.compile(r'[ ,.]')

print("Problem 13:\nReplace all occurrences of a space, comma, or dot with a colon.\n")
modified_text = pattern.sub(':', text)
print(f"Original Text: {text}")
print(f"Modified Text: {modified_text}")
print()

# Problem 14 (this is a repeat of 12?)
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
pattern = re.compile(r'\b[a|e]\w+')

print("Problem 14:\nFind all words starting with 'a' or 'e' in a given string.\n")
print(f"Text to check: {text}\n")
matches = pattern.finditer(text)
found_match = False
for match in matches:
    print(match)
    found_match = True
if not found_match:
    print("No match")
print()

# Problem 15
text = 'Python      Exercises'
pattern = re.compile(r'\s+')

print("Problem 15:\nRemove multiple spaces from a string.\n")
modified_text = pattern.sub(' ', text)
print(f"Original Text: {text}")
print(f"Modified Text: {modified_text}")

