def get_marks():
    n = int(input("Enter number of students: "))
    marks = []
    for i in range(n):
        score = int(input(f"Enter marks for student {i+1}: "))
        marks.append(score)
    return marks

def calculate(marks):
    avg = sum(marks) / len(marks) if marks else 0
    highest = max(marks) if marks else None
    lowest = min(marks) if marks else None
    return avg, highest, lowest

def main():
    marks = get_marks()
    avg, highest, lowest = calculate(marks)
    print(f"Fundamental's of Data structure's score")
    print(f"Average Score: {avg:.2f}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")

# Run the program
if __name__ == "__main__":
    main()
