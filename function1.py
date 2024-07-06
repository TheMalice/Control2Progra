def justify(text: str, LineWidth: int) -> str:
    """ Function that receives a string, and returns it justified"""

    words = text.split()
    n = len(words) # Number of words in the string
    
    # DP array to store the minimum cost of wrapping words[i:] to the end
    dp = [float('inf')] * (n + 1)
    dp[n] = 0  # No cost for wrapping an empty string
    
    # Array to store the index of the last+1 optimal word in a line.
    line_final_word = [-1] * (n)
    
    # Calculate costs for every combination, filling up dp array.
    for i in range(n - 1, -1, -1): # Starts from last -> start
        length = -1  # Initial length to account for no spacing before the first word
        for j in range(i, n):
            length += len(words[j]) + 1  # Length of words[i:j+1], adds 1 for the space (or accounting for 1st word)
            if length > LineWidth:  # If the length is bigger than LineWidth, break.
                break
            #if j == n - 1:
                cost = 0  # No extra cost for the last line
            else:
                cost = (LineWidth - (length - 1)) ** 2  ## Cost is defined as the square of the leftover
                                                        ## spaces, not the ones separating words
                                          # This is always checked, that's why it comes after the else.
            if dp[i] > cost + dp[j + 1]: ## Fills the dp array, starting from dp[n-1] since it's always bigger than dp[n] = 0          
                dp[i] = cost + dp[j + 1] ## If a cost is smaller than a previous one calculated, the higher value gets overwritten
                line_final_word[i] = j + 1  # And stores the "optimal" in the array.
    
    # Now, it's time to make the justified text, minimizing the costs.
    i = 0
    justified_text = "" # Initiator of final text

    while i < n:
        j = line_final_word[i] # j is the last optimal word in a line + 1
        line_words = words[i:j] # Retrieves the words of the line as words[i], words[i+1], ..., words[j-1]
        if j == n or len(line_words) == 1: # Condition for last line or lonely word.
            line = ' '.join(line_words)
            justified_text += line + ' ' * (LineWidth - len(line)) + '\n'
        else:
            line_length = sum(len(word) for word in line_words) # Calculates the length of the words of the line
            total_spaces = LineWidth - line_length # Calculates the ammount of spaces needed given LineWidth
            gaps = len(line_words) - 1 # Calculates the amount of gaps in the line. It's always the number of words - 1.
            even_space = total_spaces // gaps # Calculates the floor division of total_spaces in gaps, to separate them (relatively) equally.
            extra_space = total_spaces % gaps # Calculates the rest of the division of total_spaces in gaps, to add it.
            
            for k in range(gaps):
                justified_text += line_words[k] + ' ' * (even_space + (1 if k < extra_space else 0)) # adds the words in 'words[i:j-1]' (missing the last one of the line)
            justified_text += line_words[-1] + '\n' # Adds the last word in the line and starts a new line.
        
        i = j
    #print(dp)
    #print(line_final_word)
    return justified_text


