from CRUD_file import read_text_from_file, write_text_to_file, update_text_in_file, delete_text_from_file 
    
def CRUD():
    print("Please insert down below the directory and name of the file you want to process.")
    print("Example: C:\Desktop\RandomStory.txt")
    filename = input()
    if not filename:
        filename = 'E:\TestC2\RandomStory.txt'

    print(f"What do you want to do? \n 1) Read text from a file \n 2) Append (create) text to a file \n 3) Update a text file \n 4) Delete text from a file")
    print("Please write one number below:")
    answer = int(input())

    if not answer:
        return f"The user did not choose an operation."

    elif answer == 1:
        text = read_text_from_file(filename)
        print(f"Text read from '{filename}':\n{text}")
    
    elif answer == 2:
        print("Please write the text that you want to append to the file:")
        text_to_append = input()
        write_text_to_file(filename, text_to_append, mode='a')

    elif answer == 3:
        print("Please write the text you want to replace:")
        old_text = input()
        print("Now, write the new text")
        new_text = input()
        update_text_in_file(filename, old_text, new_text)

    elif answer == 4:
        print("Please write the text that you want to delete from the file:")
        text_to_delete = input()
        delete_text_from_file(filename, text_to_delete)

if __name__ == "__main__":
    CRUD()