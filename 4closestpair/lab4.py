#-----------------# Lab 4 - Closest pair #-------------------------#
#---------------------# bas15fvi #---------------------------------#

# Scheme
'''
1. sort points based on x-coord
2. Split into equal parts based on x
3. Solve recursively in left/right subsets => d_Lmin, d_Rmin
4. Compare to find min of d_Lmin, d_Rmin
5. Find d_LRmin among a subset of points that lie on different sides
# of x_mid
6. Compare to find global min

'''



#---------------# Imports #-----------------#

import sys
from math import sqrt
from itertools import combinations


#---------------# functions #--------------------#


def read_stdin():
    f = sys.stdin.read()
    lines = f.strip().split('\n')
    #nbr_players = int(lines[0])
    coords = []
    for l in lines[1:]:
        ll = l.split(" ")
        coords.append([int(lll) for lll in ll])
    return coords



# sort coords based on x
def x_sort(l):
    return sorted(l,key=lambda x: x[0])

# calculate distance between two points and update Closest
def distance(p1,p2):
    global Closest
    dx = p1[0]-p2[0]
    dy = p1[1]-p2[1]
    # TODO: if either dx or dy are larger than Closest we dont have to continue
    dist = sqrt(dx**2 + dy**2)
    if dist < Closest:
        Closest = round(dist,6)

# Go through all points. O(n^2) (only do for list of coords with len ≤ 3)
def brute(coords):
    for p1,p2 in combinations(coords,2):
        distance(p1,p2)


# Halves coords-list for even and uneven nbr of points
def divide_list(coords):
    #global nbr_players
    nbr_points = len(coords)
    half = nbr_points//2
    if nbr_points%2 == 0:
        return coords[:half], coords[half:]
    else:
        return coords[:half + 1], coords[half:]

#
def find_closest(coords):
    # brute force for ≤ 3 points
    nbr_points = len(coords)
    if nbr_points <= 3:
        return brute(coords)

    # go down recursively
    left, right = divide_list(coords)
    find_closest(left)
    find_closest(right)

    # here Best will be updated with the closest distance between points of
    # left/right side
    # we only check points that are within Best distance
    find_closest_mid(coords)


def find_closest_mid(coords):
    nbr_points = len(coords)
    x_mid = coords[nbr_points//2][0]

    # only take points that are within Best of mid (on right and left side)
    # save time by sorting on y here (not in beginning)
    interesting_points = sorted([p for p in coords if x_mid - Closest < p[0] < x_mid + Closest], key= lambda p:p[1])
    nbr_points = len(interesting_points)

    # check 7 closest (change to 15?) of each interesting point
    for i, p1 in enumerate(interesting_points[:-1]):
        for p2 in interesting_points[i+1 : min(i+7, nbr_points)]:
            distance(p1,p2)


#------------------# Global variables #-----------------------#

Closest = float("inf")

#-------------------# Start of script #-------------------------#

coords = read_stdin()
coords = x_sort(coords)
find_closest(coords)
print(format(Closest, '.6f'))
