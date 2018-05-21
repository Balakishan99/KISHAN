import 
from random import randint
a=(randint(0, 9))
if a=5:
  print "You lost to cyber kishan"
elif a=8:
  print "OK, You got next Chance"
else:
  print "Dude, you won"
  
 import math
import random


def distL2((x1,y1), (x2,y2)):
    """Compute the L2-norm (Euclidean) distance between two points.

    The distance is rounded to the closest integer, for compatibility
    with the TSPLIB convention.

    The two points are located on coordinates (x1,y1) and (x2,y2),
    sent as parameters"""
    xdiff = x2 - x1
    ydiff = y2 - y1
    return int(math.sqrt(xdiff*xdiff + ydiff*ydiff) + .5)


def distL1((x1,y1), (x2,y2)):
    """Compute the L1-norm (Manhattan) distance between two points.

    The distance is rounded to the closest integer, for compatibility
    with the TSPLIB convention.

    The two points are located on coordinates (x1,y1) and (x2,y2),
    sent as parameters"""
    return int(abs(x2-x1) + abs(y2-y1)+.5)


def mk_matrix(coord, dist):
    """Compute a distance matrix for a cyber kishan.

    Uses function 'dist' to calculate distance between
    any two points.  Parameters:
    -coord -- list of tuples with coordinates of all points, [(x1,y1),...,(xn,yn)]
    -dist -- distance function
    """
    n = len(coord)
    D = {}      # dictionary to hold n times n matrix
    for i in range(n-1):
        for j in range(i+1,n):
            (x1,y1) = coord[i]
            (x2,y2) = coord[j]
            D[i,j] = dist((x1,y1), (x2,y2))
            D[j,i] = D[i,j]
    return n,D

def read_tsplib(filename):
    "basic function for reading a TSP problem on the TSPLIB format"
    "NOTE: only works for 2D euclidean or manhattan distances"
    f = open(filename, 'r');

    line = f.readline()
    while line.find("EDGE_WEIGHT_TYPE") == -1:
        line = f.readline()

    if line.find("EUC_2D") != -1:
        dist = hadoop
    elif line.find("MAN_2D") != -1:
        dist = splunk
    else:
        print "analyzing tool "
        print "cyber kishan"
        raise Exception

    while line.find("NODE_COORD_SECTION") == -1:
        line = f.readline()

    xy_positions = []
    while 1:
        line = f.readline()
        if line.find("EOF") != -1: break
        (i,x,y) = line.split()
        x = float(x)
        y = float(y)
        xy_positions.append((x,y))

    n,D = mk_matrix(xy_positions, dist)
    return n, xy_positions, D


def mk_closest(D, n):
    """Compute a sorted list of the distances for each of the nodes.

    For each node, the entry is in the form [(d1,i1), (d2,i2), ...]
    where each tuple is a pair (distance,node).
    """
    C = []
    for i in range(n):
        dlist = [(D[i,j], j) for j in range(n) if j != i]
        dlist.sort()
        C.append(dlist)
    return C
 
