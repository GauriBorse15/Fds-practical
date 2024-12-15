# Function to sort an array using Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Function to sort an array using Selection Sort
def selection_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Find the minimum element in unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Main code to store percentages and sort the array
def main():
    # Array to store the first-year percentages of students
    student_percentages = []

    # Number of students
    n = int(input("Enter the number of students: "))

    # Input the percentage of each student
    for i in range(n):
        percentage = float(input(f"Enter percentage of student {i+1}: "))
        student_percentages.append(percentage)

    print("Before sorting:", student_percentages)

    # Ask the user to choose sorting method
    sort_method = input("Choose sorting method (bubble/selection): ").strip().lower()

    if sort_method == "bubble":
        bubble_sort(student_percentages)
        print("After Bubble Sort:", student_percentages)
    elif sort_method == "selection":
        selection_sort(student_percentages)
        print("After Selection Sort:", student_percentages)
    else:
        print("Invalid sorting method chosen!")

# Call the main function
if __name__ == "__main__":
    main()