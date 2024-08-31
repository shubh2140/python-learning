def factFunc(num):
    fact = 1
    for item in range(1, num+1):
        fact *= item
    
    print(fact)

factFunc(5)