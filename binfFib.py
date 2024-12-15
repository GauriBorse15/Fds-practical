# Function to perform Binary Search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Function to perform Fibonacci Search
def fibonacci_search(arr, x):
    n = len(arr)
    fib_m_2 = 0  # (m-2)'th Fibonacci number
    fib_m_1 = 1  # (m-1)'th Fibonacci number
    fib = fib_m_1 + fib_m_2  # m'th Fibonacci number

    while fib < n:
        fib_m_2 = fib_m_1
        fib_m_1 = fib
        fib = fib_m_1 + fib_m_2

    offset = -1

    while fib > 1:
        i = min(offset + fib_m_2, n - 1)

        if arr[i] < x:
            fib = fib_m_1
            fib_m_1 = fib_m_2
            fib_m_2 = fib - fib_m_1
            offset = i

        elif arr[i] > x:
            fib = fib_m_2
            fib_m_1 -= fib_m_2
            fib_m_2 = fib - fib_m_1

        else:
            return True

    if fib_m_1 and arr[offset + 1] == x:
        return True

    return False

# Function to input student roll numbers and search
def main():
    # Input number of students
    n = int(input("Enter the number of students who attended the training program: "))

    # Input roll numbers (sorted order expected)
    roll_numbers = []
    print(f"Enter {n} roll numbers of students (in sorted order):")
    for i in range(n):
        roll_number = int(input(f"Enter roll number {i+1}: "))
        roll_numbers.append(roll_number)
    
    # Ensure the list is sorted
    roll_numbers.sort()

    # Print sorted roll numbers
    print("\nRoll numbers of students who attended the training program (sorted):")
    print(roll_numbers)

    # Searching for a roll number using Binary Search
    roll_number_to_search = int(input("\nEnter roll number to search using Binary Search: "))
    if binary_search(roll_numbers, roll_number_to_search):
        print(f"Roll number {roll_number_to_search} attended the training program (Binary Search).")
    else:
        print(f"Roll number {roll_number_to_search} did NOT attend the training program (Binary Search).")

    # Searching for a roll number using Fibonacci Search
    roll_number_to_search = int(input("\nEnter roll number to search using Fibonacci Search: "))
    if fibonacci_search(roll_numbers, roll_number_to_search):
        print(f"Roll number {roll_number_to_search} attended the training program (Fibonacci Search).")
    else:
        print(f"Roll number {roll_number_to_search} did NOT attend the training program (Fibonacci Search).")

# Run the program
if __name__ == "__main__":
    main()
