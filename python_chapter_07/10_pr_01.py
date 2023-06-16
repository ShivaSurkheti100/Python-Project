
num = int(input("Enter the number: "))
for i in range(1, 11):
   # print(str(num) + " X " + str(i) + " = " + str(i*num)) # concatenation of string ; or use (num*i)

# use f-string in python or use concatenation of strng
  print(f"{num} X {i} = {num*i}")
