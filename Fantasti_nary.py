import json
from difflib import get_close_matches



data = json.load(open("req_data.json"))

word = input('Enter word: ')


def getMeaning(w):
    #for case sensitivity
    w = w.lower()
    #if-else to check word exist in our data or not
    if w in data:
        return data[w]
    #give matching word
    elif len(get_close_matches(w,data.keys())) > 0:
        close_match = get_close_matches(w,data.keys())[0]
        print("Did you mean %s instead? Enter Y if yes or N if no: " % close_match)
        choice = input()
        choice = choice.lower()
        if choice == 'y':
            return data[close_match]
        elif choice == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "Sorry, We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
    
def find():                        
        meaning = getMeaning(word)
        if type(meaning) == list:
                              for item in meaning:
                                          print(item)
        else:
            print(meaning)
find()

print("\n")
print("Do you want search meaning of word again :")
print("1.Yes\n2.No")

again=str(input()).lower()
#print("Do you want search meaning of word again :")
while again=='yes':
    if(again=='yes'):
        word = input('Enter word: ')
        find()
    print("\n")
    print("Do you want search meaning of word again :")
    print("1.Yes\n2.No")
    again=str(input()).lower()
    
    

                     
                         


     


        
    
            



    
    

    
