import sys

'''
Test values:
6
0 0 3 5 0 2
0 0 3 0 0 2
0 0 3 10 10 1
0 0 3 2 0 1 
0 0 3 3 0 1
0 0 3 1 0 1
'''

#Function that calculates the squared distances used in determining outside disjointness or touching from the outside
def square_distances_outside(xa, ya, ra, xb, yb, rb):
    sq_dist = (xa-xb)**2 + (ya-yb)**2
    rad_sqsum = (ra+rb)**2
    if sq_dist > rad_sqsum:
        return 1
    elif sq_dist == rad_sqsum:
        return 0
    else:
        return -1

#Function that calculates the squared distances used in determining inside disjointness or touching from the inside
def square_distances_inside(xa, ya, ra, xb, yb, rb):
    sq_dist = (xa-xb)**2 + (ya-yb)**2
    rad_sqdiff = (ra-rb)**2
    if sq_dist > rad_sqdiff:
        return 1
    elif sq_dist == rad_sqdiff:
        return 0
    else:
        return -1

#Reading in Data
t = int(input())
for line in sys.stdin:
    values = line.split()
    xa = int(values[0])
    ya = int(values[1])
    ra = int(values[2])
    xb = int(values[3])
    yb = int(values[4])
    rb = int(values[5])
	#First check concentricity (easiest check)
    if xa == xb and ya == yb:
        print("Concentric")
	#Do square sum distance analysis on circles that do not share any area (outside of each other)
    elif square_distances_outside(xa, ya, ra, xb, yb, rb) == 1:
        print("Disjoint-Outside")
    elif square_distances_outside(xa, ya, ra, xb, yb, rb) == 0:
        print("Touching")
	#Now do a square sum analysis on circles from inside
    elif square_distances_inside(xa, ya, ra, xb, yb, rb) == 1:
        print("Disjoint-Inside")
    elif square_distances_inside(xa, ya, ra, xb, yb, rb) == 0:
        print("Touching")
    else:
        print("Intersecting")