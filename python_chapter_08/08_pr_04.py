# write recursive function to calculate the sum of first n natural numbers
# factorial ko lagi; n! = (n-1)! x n 
# for sum ; sum(n) = sum(n-1) + n
# recursive function ma  directly mathematical formula used as a function 

def recur_sum(n):
    if n == 1 or n == 0: # base conditon        # if n <= 1:
        return 1                                 # return n
    else:
        return n + recur_sum(n-1)

s = recur_sum(5)
print(s)






