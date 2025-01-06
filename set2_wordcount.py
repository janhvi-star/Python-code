# Program to count the number of words in a file

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Split the content into words and count them
            words = content.split()
            word_count = len(words)
            print(f"The file contains {word_count} words.")
    except FileNotFoundError:
        print("The specified file does not exist.")
   
# Replace 'example.txt' with the path to your file
file_path = 'D:\\2024-25\\even sem\PPFSD\\Python_practical\\demo.txt'
count_words(file_path)
