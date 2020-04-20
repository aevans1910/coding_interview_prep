#Excercism code
#Test cases: "Hello, how are you?" "Great #great"
#Bad test case: "Hi 'how's' life going?" "IDK what 'his':chocolate' means."

def count_words(sentence):
    #I need to take in a sentence or string, and return the
    #number of times each word appears in that sentence. 
    #I have to create a dictionary to store the words and how
    #many times they appear. I therefore have to go through 
    #the words in the string, for each word I have to check 
    #if it already exsists in my dictionary, then I add 1 to the
    #value of that word's key. If it isn't already in the 
    #dictionary, then I add it with a value of 1.

    #Originally forgot I had to split sentence
    cleaned_up_sentence = sentence.strip('(),.?!:;*&^#').lower()
    split_sentence = cleaned_up_sentence.split()
    sentence_words = {}

    for word in split_sentence:
        if word not in sentence_words:
            sentence_words[word] = 1
        else:
            sentence_words[word] += 1
            
    return sentence_words