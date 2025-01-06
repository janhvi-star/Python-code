# Program to count the number of characters in a text file

def count_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            char_count = len(content)
            print(f"The file contains {char_count} characters.")
    except FileNotFoundError:
        print("The specified file does not exist.")
    
# Replace 'example.txt' with the path to your file
file_path = 'D:/2024-25/even sem/PPFSD/Python_practical/demo.txt'
count_characters(file_path)
