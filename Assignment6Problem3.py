# Problem 3

def translate_phone_number(phone_number):
    
    letter_to_number_table = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '22233344455566677778889999')
    
    
    get_number = phone_number.upper().translate(letter_to_number_table)
    
    return get_number

phone_number = input("Enter telephone number (XXX-XXX-XXXX): ")

get_number = translate_phone_number(phone_number)

print("Translated phone number: ", get_number)      

