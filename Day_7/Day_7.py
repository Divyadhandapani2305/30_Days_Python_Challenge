#print Numbers from 1 to 10
for i in range(1,11):
    print(i,end=" ")
    
#print square of the first 5 numbers
print("\n")
for i in range(1,6):
    print(i,"->", i*i)
    
#Sum of first 5 numbers
sum = 0
for i in range(1,6):
    sum+=i
print(sum)

#Task
n = int(input("Enter number:"))
s=0
for i in range(1,n+1):
    print(i ,end = " ")
    s+=i      
print("\n Sum of Numbers:",s)
average = sum/n
print("Avg=",average)
    
#Challenges
n = int(input("Enter Number:"))
for i in range(1,n+1):
    print(" " * (n-i) + "* " * i)
    