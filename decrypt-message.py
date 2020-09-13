"""An infamous gang of cyber criminals named “The Gray Cyber Mob”, which is behind many hacking attacks and drug trafficking, has recently become a target for the FBI. After intercepting some of their messages, which looked like complete nonsense, the agency learned that they indeed encrypt their messages, and studied their method of encryption.

Their messages consist of lowercase latin letters only, and every word is encrypted separately as follows:

Convert every letter to its ASCII value. Add 1 to the first letter, and then for every letter from the second one to the last one, add the value of the previous letter. Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII. Convert the values back to letters.

For instance, to encrypt the word “crime”

Decrypted message:	c	r	i	m	e
Step 1:	99	114	105	109	101
Step 2:	100	214	319	428	529
Step 3:	100	110	111	116	113
Encrypted message:	d	n	o	t	q
The FBI needs an efficient method to decrypt messages. Write a function named decrypt(word) that receives a string that consists of small latin letters only, and returns the decrypted word.

Explain your solution and analyze its time and space complexities."""


def decrypt(word):
  previous_letter = 0
  decrypted_word = ""
  for letter in word:
    letter = ord(letter)
    if len(decrypted_word) == 0:
      decrypted_value = int(letter - 1)
      previous_letter = letter
      decrypted_word += chr(decrypted_value)
    else:
      rounded = round(previous_letter / 26)
      step2_value = letter + rounded * 26
      decrypted_value = int(step2_value - previous_letter)
      decrypted_word += chr(decrypted_value)
      previous_letter = step2_value
  return decrypted_word

word = "dnotq"
decrypt(word)