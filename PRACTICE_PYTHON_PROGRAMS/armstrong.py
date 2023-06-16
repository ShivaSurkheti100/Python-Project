###   Python program to chekck Armstrong number
'''Armstrong number :
xyz..... = x^n + y^n + z^n +..... :::: order n
ex: 153 = 1^3 + 5^3 + 3^3 ::::::: order 3
other ex::: 0, 1, 153, 370, 371, 407, 1634, 8208, 9474, 54748
8891%10=1, 889%10=9, 88%10=8, 8%10=8: remainder le 8891 banyo
:::::::::::: In in Python >> 88/10 = 8.8 but 88//10 = 8 (floor division)::::::::::
python ma ::: ^ == ** == to the power::::
'''

n = int(input("Enter a number: "))
sum = 0
order = len(str(n))
copy_n = n ## while loop exit garda n=0 hunxa so we need copy of n
while(n>0):
    digit = n % 10 # digit = x
    sum += digit**order ## x^n
    n = n // 10

if sum == copy_n :
    print(f"{copy_n} is an Armstrong number")
else:
    print(f"{copy_n} is not an Armstrong number.")

