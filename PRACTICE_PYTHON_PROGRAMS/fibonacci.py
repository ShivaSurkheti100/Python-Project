##:::::::::Python program to print nth term of fibonacci series : iterative vs recursive approach
'''Fibonacci Series
f0 = 0, f1 = 1 : fn = fn-1 + fn-2 : f0, f1, f2, f3, f4, f5, ........
ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
prevPrevNum=0, prevNum=1, currentNum=1 (suppose)
prevPrevNum(not existed; not initialized) lai ek step agadai badaune , feri prevNum ani currentNum lai ek step  agadi badaune 
yeso garda   prevPrevNum  = prevNum : prevNum = currentNum hunxa ; tei vayerw yeso gareko
'''


import time ## time module 
def fiboIter(n):
    prevNum = 0 
    currentNum = 1
    for i in range(1, n): ## loop 1 to n-1 samma chalxa
        prevPrevNum  = prevNum  
        prevNum = currentNum
        currentNum = prevNum + prevPrevNum
    return currentNum


def fiboRecur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboRecur(n-1) + fiboRecur(n-2)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    init = time.time()
    # print(f"Using recursion approach, fib({num}) is {fiboRecur(num)}")
    print(f"Using Iterative approach, fib({num}) is {fiboIter(num)}")
    print(f"It took {time.time() - init} seconds.")

### Recursive  approach  took more time : check for num = 80