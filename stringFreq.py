def longest_word(s):
    words = s.split()  # Split the string into words
    longest = max(words, key=len)  # Find the longest word
    return longest

def char_frequency(s, char):
    return s.count(char)  # Count occurrences of the character in the string

def main():
    s = input("Enter a string: ")

    # Display the word with the longest length
    longest = longest_word(s)
    print(f"The longest word is: {longest}")
    
    # Get the character to check its frequency
    char = input("Enter a character to find its frequency: ")
    frequency = char_frequency(s, char)
    print(f"The character '{char}' appears {frequency} times in the string.")

# Run the program
if __name__ == "__main__":
    main()
