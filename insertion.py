# Function for Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Function for Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Initial gap size
    while gap > 0:
        # Perform a gapped insertion sort
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Shift elements that are greater than temp by gap positions
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reduce the gap size

# Main function
def main():
    # Input number of students
    num_students = int(input("Enter the number of students: "))

    # Input the second-year percentages of students
    percentages = []
    print(f"Enter the second-year percentages of {num_students} students:")
    for i in range(num_students):
        percentage = float(input(f"Enter percentage for student {i+1}: "))
        percentages.append(percentage)

    # Ask the user for choice of sorting method
    print("\nChoose sorting method:")
    print("1. Insertion Sort")
    print("2. Shell Sort")
    choice = int(input("Enter your choice (1/2): "))

    # Sort the array using the selected sorting method
    if choice == 1:
        insertion_sort(percentages)
        print("\nSorted using Insertion Sort:")
    elif choice == 2:
        shell_sort(percentages)
        print("\nSorted using Shell Sort:")
    else:
        print("Invalid choice!")
        return

    # Display the sorted array and top five scores
    print("\nSorted Percentages:", percentages)
    print("\nTop 5 Scores:")
    for i in range(min(5, len(percentages))):
        print(f"{percentages[i]:.2f}%")

# Run the main function
if __name__ == "__main__":
    main()
