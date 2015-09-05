#-*-coding: utf-8 -*-
import sys
import random
import numpy as np
import time

def upper_pow_2(n):
    t = 1 << 30 # 2^31
    
    while n < t:
        t >>= 1
    
    return t << 1



def brute_multiply(x, y):
    """Brute force algorithm for Matrix Multiplication"""
    
    n = x.shape[0]
    res = np.zeros(x.shape)
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i, j] += x[i, k] * y[k, j]
    
    return res

def strassen_dot(x, y):
    """
Multiplies square (nxn) matrices using Strassen's algorithm
    """
#    X = (A B)   Y = (E F)
#        (C D)       (G H)
#        
#    A through H -- (n/2 x n/2) matrices
#    
#    let P1 = A(F-H), P2 = (A+B)H, P3 = (C+D)E, P4 = D(G-E), 
#    
#        P5 = (A+D)(E+H), P6 = (B-D)(G+H), P7 = (A-C)(E+F)
#    
#    XY = (AE+BG AF+BH) = (P5+P4-P2+P6   P1+P2      )
#         (CE+DG CF+DH)   (P3+P4         P1+P5-P3-P7)

    n = x.shape[0]
    originalN = n
    
    # base case (n<=8)
    if n <= 8:
        return brute_multiply(x, y)
    
    n_is_power_of_two = (n & (n-1) == 0)

    if not n_is_power_of_two:
        # count the closest power of 2 above n
        # and resize x and y matrices
        newN = upper_pow_2(n)
        
        n = newN
        
        nX = np.zeros( (n, n) )
#        mapping x on to nX:
        nX[:originalN, :originalN] = x
        x = nX
        
        nY = np.zeros( (n, n) )
#        mapping y on to nY:
        nY[:originalN, :originalN] = y
        y = nY
        
    
    a = x[ 0:n//2, 0:n//2 ]
    b = x[ 0:n//2, n//2: ]
    c = x[ n//2:, 0:n//2 ]
    d = x[ n//2:, n//2: ]

    e = y[ 0:n//2, 0:n//2 ]
    f = y[ 0:n//2, n//2: ]
    g = y[ n//2:, 0:n//2 ]
    h = y[ n//2:, n//2: ]
    
#    let P1 = A(F-H), P2 = (A+B)H, P3 = (C+D)E, P4 = D(G-E), 
#    
#        P5 = (A+D)(E+H), P6 = (B-D)(G+H), P7 = (A-C)(E+F)
    
    # recursively compute 7 (SEVEN) products P1 .. P7
    p1 = strassen_dot(a, f-h)
    p2 = strassen_dot(a+b, h)
    p3 = strassen_dot(c+d, e)
    p4 = strassen_dot(d, g-e)
    p5 = strassen_dot(a+d, e+h)
    p6 = strassen_dot(b-d, g+h)
    p7 = strassen_dot(a-c, e+f)
    
#    do the necessary (clever) additions & substractions with P1..P7
    
#    XY = (AE+BG AF+BH) = (P5+P4-P2+P6   P1+P2      )
#         (CE+DG CF+DH)   (P3+P4         P1+P5-P3-P7)
    res1 = np.hstack( (p5+p4-p2+p6, p1+p2) )
    res2 = np.hstack( (p3+p4, p1+p5-p3-p7) )
    res = np.vstack( (res1, res2) )

    return res[:originalN, :originalN]





if len(sys.argv) == 2:
    n = int(sys.argv[1])
else:
    n = raw_input("Enter n: ")
    n = int(n)

#Input: X, Y - nxn matrices
x = np.zeros( (n, n) )
y = np.zeros( (n, n) )

for i in range(n):
    for j in range(n):
        x[i, j] = random.randint(0, 9)
        y[i, j] = random.randint(0, 9)

#print " X: \n", x
#print " Y: \n", y

start = time.time()
controlRes = np.dot(x, y)

print "\n Time for NumPy: %r" % (time.time() - start)
#print "\n[For the check-up] NumPy dot(X, Y) == \n", controlRes


start = time.time()
bruteRes = brute_multiply(x, y)
print "\n Time for Brute Multiply: %r" % (time.time() - start)
#print "\n[For the check-up] Brute Multiply == \n", bruteRes

start = time.time()
res = strassen_dot(x, y)

print "\n Time for Strassen: %r" % (time.time() - start)
#print """
#Strassen's matrix multiplication:
#    dot(X, Y) == 
#""", res

if np.all(res == controlRes):
    print "OK \n"

