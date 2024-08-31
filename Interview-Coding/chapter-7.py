# Largest Number from the List

list1 = [22, 66, 100, 45, 89, 99]

largest = list1[0]

for item in list1:
    if(largest < item):
        largest = item

print(largest)