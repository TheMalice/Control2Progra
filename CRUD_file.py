def read_text_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return None
    

def write_text_to_file(filename, text, mode='w'):
    try:
        with open(filename, mode, encoding='utf-8') as file:
            file.write(text)
        print(f"Text successfully {'appended to' if mode == 'a' else 'written to'} '{filename}'.")
    except Exception as e:
        print(f"Error writing to file '{filename}': {e}")



def update_text_in_file(filename, old_text, new_text):
    try:
        with open(filename, 'r+', encoding='utf-8') as file:
            content = file.read()
            updated_content = content.replace(old_text, new_text)
            file.seek(0)
            file.truncate()
            file.write(updated_content)
        print(f"Text successfully updated in '{filename}'.")
    except Exception as e:
        print(f"Error updating file '{filename}': {e}")



def delete_text_from_file(filename, text_to_delete):
    try:
        with open(filename, 'r+', encoding='utf-8') as file:
            content = file.read()
            updated_content = content.replace(text_to_delete, '')
            file.seek(0)
            file.truncate()
            file.write(updated_content)
        print(f"Text successfully deleted from '{filename}'.")
    except Exception as e:
        print(f"Error deleting from file '{filename}': {e}")
