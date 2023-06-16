# print sum of first n natural numbers using while loop  

n = int(input("Enter the number upto which you want to sum: "))
i = 1
sum = 0
while i<=n:
    sum += i # sum = sum + i
    i = i + 1
    
print("Required Sum is", sum)



