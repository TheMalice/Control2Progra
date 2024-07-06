from DP_functions import word_wrap, wordBreak
from function1 import justify
from CRUD_file import read_text_from_file
    
def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0
    
    if max_length == 0:
        return ""
    else:
        start_index = end_index - max_length + 1
        return s1[start_index:end_index + 1]

def function2():
    print('Please write the direction to your .doc or .txt file in the following line:')
    filename = input()
    if not filename:
        filename = 'E:\TestC2\RandomStory.txt'
    text = read_text_from_file(filename)

    print('What do you want to do? \n 1) Find Longest Common Substring \n 2) Word Break \n 3) Word Wrap \n 4) Justify the text')
    print('Please choose a number and write it below (user input):')

    answer = input()

    if not answer:
        return f'The user did not choose an option'
    
    elif int(answer) == 1:
        print('|------ Longest Common Substring with text using user input ------|')

        print('Write a word/string that you want to find in the text in the following line:')
        s1 = input()
        if not s1:
            s1 = 'NoAnswer'
        common_substring = longest_common_substring(text, s1)
        print(f"Longest common substring between the file inserted and '{s1}': {common_substring}")

    
    elif int(answer) == 2:
        
        # ---------------------------------- ------------------------------- ------
        # To be honest, I don't understand the teacher's way of explaining things
        # in the C2 pdf, what does it mean to identify Word Break?
        print('|------ Word Break by user input ------|')
        word_list = text.split()
        print('Write a string of words (without space) to see if they can be segmented by words in the file you inserted.')
        string_to_check = input()
        if not string_to_check:
            string_to_check = "CloseToYouIFeel"
        can_break = wordBreak(string_to_check, word_list)
        print(f"Can '{string_to_check}' be segmented into textfile words? {can_break}")

    elif int(answer) == 3:
        
        # ---------------------------------- ------------------------------- ------
        print('|------ Word Wrap and Justify by user input ------|')
        # Using word_list from Word Break
        print('Please, write the maximum line width for the textfile you inserted:')
        max_width = int(input())
        word_list = text.split()
        if not max_width:
            max_width = 16
        min_cost = word_wrap(word_list, max_width)
        print(f"Minimum cost of wrapping words: {min_cost}")


    elif int(answer) == 4:
        print('Please, write the maximum line width for the textfile you inserted, to format it into the desired shape:')
        max_width = int(input())
        print(f"Here you have the justified text of the file you selected \n with a maximum width of {max_width}")
        print(justify(text, max_width))
        
    

if __name__ == "__main__":
    function2()
