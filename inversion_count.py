#-*-coding: utf-8 -*-
import random
import sys


def merge_and_count_split_inv(b, c):
    """
    while merging the two sorted subarrays B and C
    increment the total number of split inversions:
        when element of 2nd subarray C gets copied to output D,
        increment total by number of elements 
        remaining in 1st subarray B
    """
    lenB = len(b)
    lenC = len(c)
    n = lenB + lenC
    
    d = [None] * n
    total = 0
    i = 0
    j = 0
    for k in range(n):
        
        left_is_empty = (i >= lenB)
        right_is_empty = (j >= lenC)
        
        # if right is empty, then left is NOT empty! (and vice versa)
        # please, don't change the order of conditions
        if right_is_empty:
            d[k] = b[i]
            i += 1
            
        elif left_is_empty:
            d[k] = c[j]
            j += 1
            
        elif b[i] < c[j]:
            d[k] = b[i]
            i += 1
            
        else:
            d[k] = c[j]
            j += 1
            total += (lenB - i)
    
    return d, total



def sort_and_count(arr):
    """
    counts number of all inversions in array 
    [left, right and split inversions]
    """
#    arr = list(arr)
    n = len(arr)
    
    if n <= 1:
        return arr, 0 
    else:
#sort left half of A and count left inversions
#B -- sorted left half
        b, x = sort_and_count( arr[  : n//2 ] )
#sort right half of A and count right inversions
#C -- sorted right half
        c, y = sort_and_count( arr[ n//2 : ] )
#count number of split inversions by merging two sorted halfs of A 
#D -- sorted A
        d, z = merge_and_count_split_inv(b, c)
        
    return d, x+y+z




if len(sys.argv) >= 2:
    n = int(sys.argv[1])
else:
    n = raw_input("Enter n -- length of array a: ")
    n = int(n)

#input: array A[n] = [0,1, ... ,n-1]
a = [None] * n
for i in range(n):
    a[i] = i

random.shuffle(a)

print "Array A: \n %r \n" % a

sortedA, numInv = sort_and_count(a)

print "Sorted A: \n %r" % sortedA
print "Number of inversions: %r \n" % numInv
