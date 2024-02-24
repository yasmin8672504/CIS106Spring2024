# Problem 4

def count_vowels(string):

    vowels = 'aeiou'

    vowels_value = sum(string.lower().count(vowel) for vowel in vowels)

    return vowels_value

def count_consonants(string):

    consonants_value = sum(1 for char in string if char.isalpha() and char.lower() not in 'aeiou')

    return consonants_value

get_string = input("Enter a string: ")

vowel_count = count_vowels(get_string)
consonant_count = count_consonants(get_string)

print("Number of vowels: ", vowel_count)
print("number of consonants: ", consonant_count)



