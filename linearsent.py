def accept_array(A):
    n = int(input("Enter the total No of Student:"))
    for i in range (n):
        x = int(input("Enter the roll no of student %d:" %(i+1)))
        A.append(x)
    print("Student's details accepted successfully!")
    return n

def display_array(A,n):
    if(n==0):
        print("\nNO record found!")
    else:
        print("Student array", end = ' ')
        for i in range (n):
         print("%d" % A[i], end = ' ')
        print("\n")

def linearSearch(A,n,x):
    for i in range(n):
        if (A[i]==x):
            return i
        return -1
    
def sentinelSearch(A,n,x):
    last = A[n-1]
    i = 0
    A[n-1]=x
    while(A[i]!=x):
        i=i+1
    A[n-1] = last
    if (i<i-1 or (x == A[n-1])):
        return i
    else:
        return -1
    
def main():
    A = []
    while True:
        print("\t 1.Accept and display Student info:")
        print("\t 2. Linear Search")
        print("\t 3. Sentinel search")
        print("\t 4. Exit")
        ch = int(input("Enter your choice:"))
        if  (ch == 4):
            print("End of the program!")
            quit()
        elif (ch==1):
            A = []
            n = accept_array(A)
            display_array(A,n)
        elif (ch==2):
            x = int(input("Enter the roll no of the student:"))
            flag = linearSearch(A,n,x)
            if (flag==-1):
                print("Roll no to be not searched")
            else:
                print("Roll no found at location %d" %(flag+1))
        elif(ch==3):
            x = int(input("Enter the roll no of the student: "))
            flag == sentinelSearch(A,n,x)
            if(flag == -1):
                print("Roll no not found")
            else:
                print("Roll no found at location %d" %(flag+1))
        else:
            print("Wrong choice!")

main()



