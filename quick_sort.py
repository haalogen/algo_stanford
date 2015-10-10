#-*-coding: utf-8 -*-
import sys
import numpy as np
import time
import copy


def qsort(array):
    _qsort(array, 0, len(array) - 1)


def _qsort(array, start, stop):
#    [start, stop]
    if stop - start > 0:
        randPos = np.random.randint(start, stop+1)
        pivot, left, right = array[randPos], start, stop
        
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
                
        _qsort(array, start, right)
        _qsort(array, left, stop)
        

def _selectsort(array):
    N = len(array)
    
    
    for k in range(N):
        minInd = k
        for i in range(k+1, N):
            if array[i] < array[minInd]:
                minInd = i
#                print "min: ", array[minInd] 
            
        array[k], array[minInd] = array[minInd], array[k]



def qsort_select(array, m):
    _qsort_select(array, 0, len(array) - 1, m)


def _qsort_select(array, start, stop, m):
#    [start, stop]
    if stop - start + 1 > m: # more than m elements
        randPos = np.random.randint(start, stop+1)
        pivot, left, right = array[randPos], start, stop
        
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
                
        _qsort_select(array, start, right, m)
        _qsort_select(array, left, stop, m)
    else:
#        print ("selection_sort")
        _selectsort(array[start : stop+1])





# MAIN
N = 6
m = 6
times = 10

if len(sys.argv) >= 4:
    N = int(sys.argv[1])
    m = int(sys.argv[2])
    times = int(sys.argv[3])
else:
    print """Usage: 
python quick_sort.py [len_array] [len_selectsort] [num_experiments]
Ex:
    python quick_sort.py 10 10 10
"""
    sys.exit(-1)

    
A = np.random.randint(0, 10, N)
#A = np.random.random(N)
#print "A: \n", A

startTime = time.time()
timA = np.array( sorted(A) )
print "Timsort time: ", time.time() - startTime

qsortA = copy.deepcopy(A)
print "Starting qsort..."
startTime = time.time()
qsort(qsortA)
#print "QSort: \n", qsortA
print "QSort time: %r sec", time.time() - startTime 
print "QSort is correct: ", all(timA == qsortA)

if N <= 1000:
    selA = copy.deepcopy(A)
    print "Starting selection_sort..."
    startTime = time.time()
    _selectsort(selA)
    #print "QSort: \n", qsortA
    print "SelectionSort time: %r sec", time.time() - startTime 
    print "SelectionSort is correct: ", all(timA == selA)
#    print selA


qselA = copy.deepcopy(A)
print "Starting QSort_select, m = %r..." % m
startTime = time.time()
qsort_select(qselA, m)
#print "QSort: \n", qsortA
print "QSort_select time: %r sec", time.time() - startTime 
#print qselA
print "QSort_select is correct: ", all(timA == qselA)
