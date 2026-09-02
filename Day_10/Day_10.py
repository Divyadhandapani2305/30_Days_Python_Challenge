#TASK
my_list=[10,20,40,60,80]
print("original_list:",my_list)

my_list.append(100)
print("After Add:",my_list)
my_list.insert(3,45)
print("After insert:",my_list)

my_list.remove(20)
print("After Remove:",my_list)

print("Length:",len(my_list))

#CHALLENGE
nums = list(map(int,input("Enter Number:").split()))
print("Max:",max(nums))
print("Min:",min(nums))
print("Reversed:",nums[::-1])
print("Sorted:",sorted(nums))