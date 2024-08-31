tup = (10, 23, 41, 56, 89, 33, 66, 0, 98)
i=0
num = 0
while i < len(tup):
    if(tup[i] == num):
        print("Found", i)
    else:
        print("Not Found")
    i+=1