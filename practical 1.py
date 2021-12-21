number = int(input("enter number of students: "));
list1=[]
for i in range(number):
  marks=int(input(f"enter marks of {i} students"))
  list1.append(marks)
def main():
  print("1.Display the marks ")
  print("2.Find the Sum and Average of the marks ")
  print("3.Find the maximum marks ")
  print("4.Find the minimum marks ")
  print("5.Find the highest frequency of reapeated marks ")
  print("6.Find the number of absent students ")
  print("7.Exit")
  while True:
    ch = int(input("Enter a choice for operation:"))
    if ch==1:
      display()
    if ch==2:
      total_avg()
    elif ch==3:
      maximum_marks()
    elif ch==4:
      minimum_marks()
    elif ch==5:
      highest_freq()
    elif ch==6:
      absent()
    if ch==7:
      break
def display():
  print(f"The List contains these marks: {list1}")

def total_avg():
  sum=0;
  count=0
  count=len(list1)
  for i in range(len(list1)):
    sum+=list1[i]
  avg= sum/count
  print(f"sum of marks are:{sum}")
  print(f"avg of marks are:{avg}")

def max_min(): 
  max = list1[0]
  for i in range(len(list1)):
    if(max<list1[i]):
      max = list1[i]
  print(f"maximum marks are: {max}")

def highest_freq():
  counter=0
  result=list1[0]
  for i in list1:
    frequency=list1.count(i)
    if frequency>counter:
      counter = frequency
      result = i
  print(f"frequent marks :",result)

def minimum_marks():
  for i in range(len(list1)):
    if(list1[i]!=-1):
      min = list1[i]
      break
    for j in range(len(list1)):
      if (list1[j]!=-1):
        if (min>list1[j]):
          min = list1[j]
  print(f"minimum marks are:{min}")

def absent():
  count=0
  for i in range(len(list1)):
    if(list1[i]==-1):
      count=count+1
  print(f"Absent students count is: {count}")

if __name__=="__main__":
  main()