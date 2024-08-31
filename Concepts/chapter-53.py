tup = (33, 44, 23, 99, 90, 56, 45, 34)
x=45
count = 0
for item in tup:
    if(item == x):
        print("Found", count)
        break
    count += 1