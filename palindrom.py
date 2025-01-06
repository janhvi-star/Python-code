# Input string
string = input("Enter a string: ")

# Remove spaces and convert to lowercase for case-insensitive comparison
string = string.replace(" ", "").lower()

# Initialize pointers
start = 0
end = len(string) - 1

# Check for palindrome
is_palindrome = True
while start < end:
    if string[start] != string[end]:
        is_palindrome = False
        break
    start += 1
    end -= 1

# Output result
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
