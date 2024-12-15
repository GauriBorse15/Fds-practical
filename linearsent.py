def accept_array(A):
    n = int(input("Enter the no. of students"))
    for i in range(n):
        x = int(input("\nEnter the roll no of student %d:", %(i+1)))
        A.append(x)
    print("Student information accepted successfully!")

def display_array(A,n):
    if(n==0):
        print("\nNo records found!")
    else:
        print("Student's Array:", end = ' ')
        for i in range(n):
            print("%d" % A[i], end = ' ')
        print("\n")

def linear_search(A,n,x):
    for i in range(n):
        if(A[i]==x):
            return i
        return -1
def main():
    A = []
    while True:
        print("\t 1. Accept and Display array info:")
        print("\t 2. Linear search:")
        print("\t 3. Exit")

        ch = int(input("Enter your choice:"))
        if (ch==4):
            print("End of the program. \nThank you!")
            quit()