import json 
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(word , data.keys())[0])
        decide = input("press y for yes or n for no\n")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return ("Word doesn't exist\n")
        else:
            return("you have entered a wrong choice\n")
    else:
        print("Wrong word or spelling mistake. please check!!\n")
word = input("enter the word you want to search\n")
meaning_word = meaning(word)
if type(meaning_word) == list:
    for item in meaning_word:
        print(item)
else:        
    print(meaning_word)