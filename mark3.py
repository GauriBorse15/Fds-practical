marks=[]
present=[]
absent=[]
n=0
def marksobtain():
 global n
 n=int(input("Enter the number of students:\n"))
 print("The marks of the absent student is 0")
 for i in range(1,n+1):
  print ("Enter marks of student ",i,":")
  s=int(input())
  marks.append(s)
  if (s>0):
   present.append(s)
  else:
   absent.append(s)
 print("Marks of the students :",marks)
def average():
 a=0
 for i in present:
  a=a+i
  average=(a/len(present))
 print("Average marks of the students is",average) 
def high_low():
   print("Highest Marks :",max(present))
   print("Lowest Marks :",min(present))
   
def absent_length():
   print("Number of absent students :",len(absent))   
   
def frequency():
   print("Marks with the highest frequency :",max(set(present),key=present.count))
   
marksobtain()
average()
high_low()
absent_length()
frequency()

