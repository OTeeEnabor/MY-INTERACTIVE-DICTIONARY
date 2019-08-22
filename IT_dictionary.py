"""
This script is for an interactive Python dictionary. The dictionary contains
IT words that in my vocabulary. I will regularly update the dictionary as my
vocabulary increases.
"""

# import the following libaries that will be used in this script.
import json
import difflib
from difflib import get_close_matches

#Create a dictionary function
def dictionary(word):
    #load the dictionary and store it as variable name => data
    data = json.load(open('data.json'))
    #get a list of the words in the dictionary and store it as variable name => dict_keys
    dict_keys = data.keys()
    #Capitalize the first letter of each word
    word = word.title()
    #The get_close_matches() will look for the keys that match the word inputed by the user
    #if the user enters a word that does not return a list, then an error will occur and the else statement will run

    try:

        best_match = get_close_matches(word,dict_keys)[0]
        #If the
        #code to run if word is not in the dictionary and there is a close match to the word
        if word not in data:
        #Suggest a word similar to the user input and ask the user to answer if this is the word they were trying to search for.
            decide = input("Did you mean %s? Enter Y if yes,  enter N if no... " %best_match )
        #If the user enters a  response that is not a string, enter a while loop:
            while decide.isalpha() == False:
                decide = input("Please enter Y for Yes and N for No: ")
        #If the user enters a string break out the loop
                decide.isalpha()
        #If the user enters a Y or y then run the following code:
            if (decide.lower() =='y' or decide.upper() == 'Y') and (type(data[best_match]) == list) :
                #Return output by iterating through the list and return
                dic_output = data[best_match]

                for item in data[best_match]:
                    print(item,sep="")
            else:
                print("Sorry, the word you are looking for is not in this dictionary.")
        else:
            for item in (data[word]):
                print(item)
    except:
        print('Sorry, the word you entered is not in this dictionary.')

    #if the word is not in the dictionary run;

server= input('please enter word: ')
serv = dictionary(server)
