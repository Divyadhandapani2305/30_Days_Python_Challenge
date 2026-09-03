S1= set(map(int,input().split()))
S2=set(map(int,input().split()))
print("Union:", S1|S2)

print("Intersection:",S1&S2)

print("Difference:",S1-S2)

is_subset = S1.issubset(S2)
is_superset = S1.issuperset(S2)