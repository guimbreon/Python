import random
import string
#COUNT THE AMOUNT OF DIFFERENT LETTERS
def different(quote):
    diff=""
    for thing in quote:
        if thing not in diff:
            diff+=thing
    return diff
#See all the diferent letters
def substitution(diff):
    letter_sub={}
    for letter in diff:
        letter_sub[letter]=''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=5))

    return letter_sub
#Encripting
def encripting(quote):
    encripted=""
    for letter in quote:
        encripted+=letter_sub[letter]
    return encripted
#Creates the key
def writing_key(letter_sub):
    with open(input("What file do u want to put the doc_keys?\n>>"), "w") as file:    
        for letter in letter_sub:
            file.write(f">{letter}\n{letter_sub[letter]}\n")

#FUNCTION CALLING
quote=input("Which quote to you want to encript?\n>>")
diff=different(quote)
letter_sub=substitution(diff)
encripted=encripting(quote)
writing_key(letter_sub)
print(f"\n{encripted}\n") #Tells the user what the encripted item is!