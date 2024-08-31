def factFun(num):
    fact=1
    if(num == 0):
        return
    
    fact*=num
    print(fact)
    factFun(num-1)

factFun(5)