#-*-coding: utf-8 -*-
import time
import sys
import math

def karatsuba_multiply(x, y):
    # x == 10^(n/2) * a + b ; y == 10^(n/2) * c + d
    # a, b, c, d -- n/2-digit numbers 
    # x*y = 10^n * ac + 10^(n/2) * (ad + bc) + bd
    #
    # Idea: recursively compute ac, ad + bc, bd,
    # then compute x*y in the straightforward way
    # (ad + bc) == (a + b)*(c + d) - ac - bd

    # find out n
    nx = len( str(x) )
    ny = len ( str(y) )
    n = max(nx, ny)
    
    # recursion base:
    if  n == 1:
        return x * y
    
    is_odd = ( n % 2 == 1 )
    if is_odd:
        n += 1
        
    # extract a, b, c, d for x and y
    factor = (n)//2
    
    a = x // 10**(factor)
    b = x % 10**(factor)
    
    c = y // 10**(factor)
    d = y % 10**(factor) 
    
    print a, b, c, d

    # recursively compute ac
    ac = karatsuba_multiply(a, c)
    
    # recursively compute bd
    bd = karatsuba_multiply(b, d)
    
    #compute (ad + bc) == (a + b)*(c + d) - ac - bd
    adPlusBc = karatsuba_multiply(a + b, c + d) - ac - bd
    
    # return (x*y) == 10^n * ac + 10^(n/2) * (ad + bc) + bd
    return 10**n * ac + 10**(factor) * adPlusBc + bd



# input x and y -- multiplied numbers
if len(sys.argv) != 3:
    print "Usage: python karatsuba_multiplication.py 1234 5678"
    sys.exit(-1)
    

x = sys.argv[1]
y = sys.argv[2]
x = int(x)
y = int(y)


start = time.time()
# multiply python-algorithm
res = x * y
print res
print "Python multiplication algo: \t %f sec \n" % (time.time() - start)


start = time.time()
# multiply karatsuba
res = karatsuba_multiply(x, y)
print res
print "My Karatsuba multiplication: \t %f sec \n" % (time.time() - start)

print "Yay! It works!"
