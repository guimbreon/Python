import sys

#get everything from the file and transform it into a dictionary
letter_sub={}
letters=[]
subs=[]

try:
    if sys.argv[1]=="":
        print("a")
except:
    print("You have to put this script followed by the key-file!\n")
    quit()

encripted=input("What's the encripted message u want to translate?")
def info(encripted,file):
    with open(file, "r") as file:
        for line in file:
            if line.startswith(">"):
                letters.append(line.replace("\n","").replace(">",""))
            else:
                subs.append(line.replace("\n",""))
    i=0
    for thing in letters:
        letter_sub[subs[i]]=thing
        i+=1
    return subs,letter_sub
subs,letter_sub=info(encripted,sys.argv[1])
#translation
def translation(encripted,subs,letter_sub):
    divided=[]
    while encripted!="":
        divided.append(encripted[:5])
        encripted=encripted[5:]


    for item in subs:
        if item not in divided:
            print("The encripted message CANNOT be translated by the doc_key!\n")
            quit()

    quote=""
    for item in divided:
        quote+=letter_sub[f"{item}"]
    return quote
quote=translation(encripted,subs,letter_sub)
#The translated quote!
print(quote)