#Factorial
n = int(input("Enter Number:"))
fact = 1
i = 1
while i <=n:
    fact*=i
    i = i+1
print("Factorial is :", fact)

#Task
N=int(input("Enter Number:"))
i=1
sum=0
while i<=N:
    sum+=i
    i=i+1
print("Sum:",sum)

#Challenge
secret = int(input("Enter Number:"))
guess=0
atempts=0
while guess!=secret:
    guess = int(input("Guess the Number:"))
    atempts+=1
    if guess>secret:
        print("Too high")
    elif guess<secret:
        print("Too Low")
print("Correct!")
print("Attempts:",atempts)

