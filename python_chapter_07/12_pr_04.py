
# prime number ko factor 1 and number itself

num = int(input("Enter the number: "))
prime = True
for i in range(2,num): # i vaneko range ko numbers hunn
    if(num%i == 0): # 2 dekhi num samma junsukai number le divide garda...remaider 0 aayo vane... its not prime
        prime = False
        break
if(prime):
    print("This number is prime")
else:
    print("This number is not Prime")
    



