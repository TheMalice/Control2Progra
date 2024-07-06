#|------------------------ Word Wrap ------------------------|#
def word_wrap(words, max_width):
    n = len(words)
    
    # Calculate the cost of putting words from i to j in one line
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        cost[i][i] = max_width - len(words[i])
        for j in range(i + 1, n):
            cost[i][j] = cost[i][j - 1] - len(words[j]) - 1
    
    for i in range(n):
        for j in range(i, n):
            if cost[i][j] < 0:
                cost[i][j] = float('inf')
            else:
                cost[i][j] = cost[i][j] ** 2

    # dp[i] will be the minimum cost to arrange words from 0 to i
    dp = [float('inf')] * n
    result = [0] * n
    for j in range(n):
        if cost[0][j] != float('inf'):
            dp[j] = cost[0][j]
            result[j] = -1
        for i in range(j):
            if dp[i] != float('inf') and cost[i + 1][j] != float('inf') and dp[i] + cost[i + 1][j] < dp[j]:
                dp[j] = dp[i] + cost[i + 1][j]
                result[j] = i

    # Reconstruct the solution
    lines = []
    j = n
    while j > 0:
        i = result[j - 1]
        if i == -1:
            lines.append(" ".join(words[:j]))
            break
        lines.append(" ".join(words[i + 1:j]))
        j = i + 1
    lines.reverse()
    return dp[n - 1]

#|------------------------ Word Break ------------------------|#

# A Dynamic Programming based program to test whether a given String can
# be segmented into space separated words in dictionary

# A utility function to check whether a word is present in dictionary or not.
# An array of Strings is used for dictionary. Using array of Strings for
# dictionary is definitely not a good idea. We have used for simplicity of the
# program
def dictionaryContains(word, dictionary):
    size = len(dictionary)
    for i in range(size):
        if (dictionary[i]== word):
            return True
    return False

# Returns True if String can be segmented into space separated
# words, otherwise returns False
def wordBreak(Str, dictionary):
    size = len(Str)
    if (size == 0):
        return True

        # Create the DP table to store results of subproblems. The value wb[i]
        # will be True if str[0..i-1] can be segmented into dictionary words,
        # otherwise False.
    wb = [False for i in range(size + 1)]

    for i in range(1,size + 1):
        # if wb[i] is False, then check if current prefix can make it True.
        # Current prefix is "str.substring(0, i)"
        if (wb[i] == False and dictionaryContains(Str[0: i], dictionary)):
            wb[i] = True

        # wb[i] is True, then check for all subStrings starting from
        # (i+1)th character and store their results.
        if (wb[i] == True):
            # If we reached the last prefix
            if (i == size):
                return True

            for j in range(i + 1,size + 1):
                # Update wb[j] if it is False and can be updated
                # Note the parameter passed to dictionaryContains() is
                # subString starting from index 'i' and length 'j-i'
                if (wb[j] == False and dictionaryContains(Str[i: j], dictionary)):
                    wb[j] = True

                # If we reached the last character
                if (j == size and wb[j] == True):
                    return True
                
            

    # If we have tried all prefixes and none of them worked
    return False