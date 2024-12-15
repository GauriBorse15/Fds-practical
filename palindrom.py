def is_palindrome(s):
    # Check if the string is equal to its reverse
    return s == s[::-1]

def find_substring(s, sub):
    # Return the index of the first appearance of the substring
    return s.find(sub)

def main():
    s = input("Enter a string: ")
    
    # Check if the string is a palindrome
    if is_palindrome(s):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
    
    # Find the first appearance of a substring
    sub = input("Enter a substring to find its first appearance: ")
    index = find_substring(s, sub)
    
    if index != -1:
        print(f"The first appearance of '{sub}' is at index {index}.")
    else:
        print(f"'{sub}' is not found in the string.")

# Run the program
if __name__ == "__main__":
    main()