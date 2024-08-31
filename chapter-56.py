num = int(input("Enter the number : "))
sum = 0

for i in range(1, num+1):
    sum+=i

print(sum)

fact = 1
for i in range(1, num+1):
    fact *= i

print("factorial is ", fact)