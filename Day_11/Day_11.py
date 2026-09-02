print("================ Task ================")
my_tuple = ('Apple','Banana','Grapes','Mango','Apple')
print("First Fruit:",my_tuple[0])
print("Last Fruit:",my_tuple[-1])
print("Count of 'Apple':",my_tuple.count('Apple'))
print("Is 'mango' Present:", "Mango" in my_tuple)
print("Length of tuple:",len(my_tuple))

print("================ Challenge ================")
n = int(input("Enter numbers:"))
numbers = tuple(map(int,input("Enter Numbers seperated by space:").split()))
print("Max:",max(numbers))
print("Min:",min(numbers))
e_count = 0
for num in numbers:
    if num%2==0:
        e_count+=1
print("Even Count:",e_count)
print("Reversed:",numbers[::-1])