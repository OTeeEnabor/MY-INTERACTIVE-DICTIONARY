import json
import difflib
from difflib import get_close_matches

#Create a dictionary function
def dictionary(word):
    #load the dictionary and store it into a Python dictionary
    data = json.load(open('data.json'))
    #get all the words(dictionary keys) in the dictionaty and store it into a variable
    dict_keys = data.keys()
    #the words in the dictionary start with a capital letter, therfore for our purposes capitalize the user input
    word = word.title()
    #This program should allow for the user to check for words more than once.
    satisfied = False
    while satisfied is not True:
        if word in data:
            for item in data[word]:
                print(item)
                new_entry = input("Would you like to search for another word? Enter Y for Yes and N for No")
                if (new_entry.lower() == 'n' or new_entry.upper()=="N"):
                    satisfied = True
                else:
                    new_word = input("Please enter a word: ")
                    new_search = dictionary(new_word)
#if word not in dictionary but there is a similar word in the dictionary
        elif (word not in data) and (len(get_close_matches(word,dict_keys)[0]) >= 1):
            best_match = get_close_matches(word,dict_keys)[0]
            decide = input("Did you mean %s? Enter Y if yes,  enter N if no... " %best_match )
            while decide.isalpha() == False:
                decide = input("Please enter Y if Yes or N for No: ")
                decide.isalpha()
            if (decide.lower() =='y' or decide.upper() =='Y') and (type(data[best_match]) == list):
                for item in data[best_match]:
                    print (item)
                    new_entry = input("Would you like to search for another word? Enter Y for Yes and N for No")
                    if (new_entry.lower() == 'n' or new_entry.upper()=="N"):
                        satisfied = True
                    else:
                        new_word = input("Please enter a word: ")
                        new_search = dictionary(new_word)
            else:
                print("Sorry, the word you are looking for is not in this dictionary.")
        else:
            print("Sorry, the word you are looking for is not in this dictionary.")

check = input("please enter a word: ")

dictionary(check)
