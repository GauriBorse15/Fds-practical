#include <iostream>
#include <stack>
#include <cctype>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;

// Function 1: To check if the string is a palindrome using a stack
bool isPalindromeUsingStack(const string& str) {
    stack<char> charStack;
    
    // Push all characters of the string into the stack
    for (char c : str) {
        charStack.push(c);
    }
    
    // Compare each character with the characters popped from the stack
    for (char c : str) {
        if (c != charStack.top()) {
            return false;  // If mismatch, it's not a palindrome
        }
        charStack.pop();
    }
    
    return true;  // If all characters match, it's a palindrome
}

// Function 2: To remove spaces, punctuation, and convert to lowercase, then check palindrome
bool checkPalindromeWithCleaning(string str) {
    string cleanedStr = "";
    
    // Remove spaces and punctuation, and convert to lowercase
    for (char& c : str) {
        if (isalnum(c)) {
            cleanedStr += tolower(c);
        }
    }
    
    // Call the palindrome checking function
    return isPalindromeUsingStack(cleanedStr);
}

// Function 3: To print string in reverse order using a stack
void printReverseUsingStack(const string& str) {
    stack<char> charStack;
    
    // Push all characters into the stack
    for (char c : str) {
        charStack.push(c);
    }
    
    // Pop all characters from the stack and print them to get the reverse
    while (!charStack.empty()) {
        cout << charStack.top();
        charStack.pop();
    }
    cout << endl;
}

int main() {
    string input;
    
    // Get input from user
    cout << "Enter a string: ";
    getline(cin, input);
    
    // 1. Check if the string is a palindrome using a stack
    if (isPalindromeUsingStack(input)) {
        cout << "The string is a palindrome." << endl;
    } else {
        cout << "The string is not a palindrome." << endl;
    }
    
    // 2. Check for palindrome after cleaning input (removing spaces, punctuation, and lowercasing)
    if (checkPalindromeWithCleaning(input)) {
        cout << "The cleaned string is a palindrome." << endl;
    } else {
        cout << "The cleaned string is not a palindrome." << endl;
    }
    
    // 3. Print the string in reverse order using stack
    cout << "The string in reverse order is: ";
    printReverseUsingStack(input);
    
    return 0;
}
