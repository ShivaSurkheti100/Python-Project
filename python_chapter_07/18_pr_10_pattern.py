# write a program to print multiplication table of n using for loop in reversed order


num = int(input("Enter the number: "))
for i in range(10, 0, -1): 
    print(str(num) + " X " + str(i) + " = " + str(i*num)) # concatenation of string ; or use (num*i)

# use f-string in python or use concatenation of strng
 # print(f"{num} X {i} = {num*i}")
