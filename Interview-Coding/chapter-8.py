# Smallest Number from List

list1 = [44, 66, 90, 2, 55, 78]

smallest = list1[0]

for item in list1:
    if(item < smallest):
        smallest = item

print(smallest)