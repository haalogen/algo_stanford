#-*-coding: utf-8 -*-
import sys
import random
import time

def merge_sort(arr):
    n = len(arr)
    
#    base case
    if n in [0, 1]:
        return arr
        
#    recursively sort left half of arr 
    left = merge_sort( arr[ 0 : n//2 ] )
    
#    recursively sort right half of arr
    right = merge_sort( arr[ n//2 : ] )
    
    i = 0 # index for left half
    j = 0 # index for right half
    leftN = len(left)
    rightN = len(right)
    # sorted array (result) of length n, initialized with -2n values
    resArr = [None] * n
    
#    merge two sorted sublists in one
    for k in range(n):
        
        left_is_empty = (i >= leftN)
        right_is_empty = (j >= rightN)
        
        # if right is empty, then left is NOT empty! (and vice versa)
        # please, don't change the order of conditions
        if right_is_empty:
            resArr[k] = left[i]
            i += 1
            
        elif left_is_empty:
            resArr[k] = right[j]
            j += 1
            
        elif left[i] < right[j]:
            resArr[k] = left[i]
            i += 1
            
        else:
            resArr[k] = right[j]
            j += 1
            
    
    return resArr



if len(sys.argv) == 1:
    n = 5
else:
    n = sys.argv[1]
    n = int(n)
    
a = []
for i in range(n):
    a.append(random.randint(-n, n))


print "Original array: \n %r \n" % a

start = time.time()

b = merge_sort(a)
print "Sorted array: \n %r \n" % b
print "Sorting time: %r sec \n" % (time.time() - start)

start = time.time()
c = sorted(a)
print "Python built-in sorting algorithm: %r sec \n" % \
            (time.time() - start)
print " %r" % c

