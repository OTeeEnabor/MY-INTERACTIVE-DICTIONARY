"""
This script is for an interactive Python dictionary. The dictionary contains
IT words that in my vocabulary. I will regularly update the dictionary as my
vocabulary increases.
"""

# import json
import json
import difflib
from difflib import get_close_matches

#
# #load the it dictionary json file into a python dictionary.
# it_dictionary = json.load(open("data.json"))
# # print(it_dictionary)
# for key in it_dictionary:
#     print (key)

#Create a dictionary function
def dictionary(word):
    #load the dictionary and store it as variable name => data
    data = json.load(open('data.json'))
    # get a list of the words in the dictionary and store it as variable name => dict_keys
    dict_keys = data.keys()
    #Capitalize the first letter of each word
    word = word.title()
    try:
        best_match = get_close_matches(word,dict_keys)[0]
        #Word is not in the dictionary but there is a close match to the word
        if word not in data:
            #Suggest a word similar to the user input, make sure the user enters a word
            decide = input("Did you mean %s? Enter Y if yes,  enter N if no... "%best_match )
            #If the user enters a  run a while loop
            while decide.isalpha() == False:
                decide = input("Please enter Y for Yes and N for No: ")
                decide.isalpha()
            if decide.lower() =='y' or decide.upper() == 'Y':
                print(data[best_match])
            else:
                print("Sorry, the word you are looking for is not in this dictionary.")
        else:
            print(data[word])
    except:
        print('Sorry, the word you entered is not in this dictionary.')

    #if the word is not in the dictionary run;



server= input('please enter word: ')
serv = dictionary(server)
