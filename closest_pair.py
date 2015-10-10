#-*-coding: utf-8 -*-
import sys
import random
import time
import math

def dist(p, q):
#    Euclidian 2D distance between points p(x1, y1) and q(x2, y2)
    return math.sqrt( (p[0]-q[0])**2 + (p[1]-q[1])**2 )

# BruteForce algorithm of Closest Pair
def naive_closest_pair(p):
    
    
    return [[-228, -228], [228, 228]]



# Recursive algorithm of Closest Pair
def recursive_closest_pair(p):
    
    
    return [[228, 228], [-228, -228]]




#main code
if len(sys.argv) == 2:
    n = int(sys.argv[1]) # number of points
    
else:
    print """
Usage:
    python closest_pair.py [num_of_points]
Example:
    python closest_pair.py 5
"""

#generate n random points = [x, y]
points = [None] * n

for i in range(n):
    # random.random() => [0.0, 1.0)
    points[i] = [random.random(), random.random()]

print points, "\n"

start = time.time()
# BruteForce algorithm of Closest Pair
closestCtrl = naive_closest_pair(points)

print "Closest Pair for BruteForce algorithm: %r" % closestCtrl
print "Time: %r \n" % (time.time() - start)


start = time.time()
# Recursive algorithm of Closest Pair
closest = recursive_closest_pair(points)

print "Closest Pair for Recursive algorithm: %r" % closest
print "Time: %r \n" % (time.time() - start)


if closest == closestCtrl:
    print "OK"
else:
    print "[!] Error: closest != closestCtrl"
