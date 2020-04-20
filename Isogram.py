#Code from Exercism

#Test cases: "Isogram", "Inside", "make corgi buns"
#Bad test cases: ["hey"], a very long text

def is_isogram(string):
    #Make a hashtable - a set
    #While there are still letter in the word that we 
    # have not checked
    #Check if that letter is already in the set. If not
    #add it to the set, if it is, break out of the loop and
    #raise a message saying it is not a isogram

    are_you_an_isogram = set()

    for char in string:
        if char.isalpha():
            char = char.lower()
            if char in are_you_an_isogram:
                return False
            else:
                are_you_an_isogram.add(char)
                print(are_you_an_isogram)
    return True