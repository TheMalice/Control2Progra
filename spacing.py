def justified(string: str, LineWidth: int) -> str:
     """
     Receives a string and distributes the words in it in function of the LineWidth given.
     """
     wordbyword = string.split() # List of words in the string
     words_number = len(wordbyword) # Number of words in the string
     N_words = len(wordbyword) # Number of words used for case where just one word is in the string
     WholeText= "" # Initiator
     for word in wordbyword: # Takes all the words in the string and concatenates them
          WholeText += word
     size_all_words = len(WholeText) # gets the length of the string without spaces
     ## This also could be done by iterating over 'wordbyword' and getting the length of every string.
     ## But I chose this because it's easier for me to imagine.

     space_count = LineWidth-size_all_words # Calculates the number of spaces that need to be added

     final_text = "" # Initiator of the justified and distributed text
     for i in range(words_number):
          if N_words == 1:
               final_text += wordbyword[0] + space_count*' '
          elif words_number == 1:
               final_text += space_count*' ' + wordbyword[i]
          else:
               aux = space_count//words_number + 1
               final_text += wordbyword[i] + aux*' '
               words_number = words_number - 1
               space_count = space_count - aux
     return final_text

def maxLength(string: str, LineWidth: int) -> list:
     """
     Takes a string and separates it into multiple substrings, 
     which length cannot surpass the indicated limit.
     """
     wordbyword = string.split() # Lists all the words in the string.
     final = [] # Initiator list for the output of the function.
     substring = "" # Initiator for the multiple substrings to be created.
     n = len(wordbyword)
               
     for i in range(n):
          if len(substring) + len(wordbyword[i]) + 1 > LineWidth:
               final.append(substring)
               substring = wordbyword[i]
          elif i == 0: # This makes sure that the first word doesn't have a space before it
               substring += wordbyword[i]   
          else:
               substring += ' '+ wordbyword[i]
     final.append(substring)
     return final


gpt = 'Tengo muchas cosas que hacer pero a veces me vuelvo loco'
print(justified(gpt, 100))

