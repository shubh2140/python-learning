# Palindrome List

lists1 = [1, 2, 3, 3, 2, 1]

list2 = lists1.copy()
list2.reverse()
print(list2)

if(lists1 == list2):
    print("Palindrome List")
else:
    print("Not a Palindrome")