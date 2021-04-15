"""Write a function to reverse an integer, without using any intermediate storage except for other integer values.

"""
n = 1234
n_rev = 0
while n :
    ld = n%10
    n_rev = n_rev*10 + ld
    n//=10
print(n_rev)
