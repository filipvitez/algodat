
# ---------------# Problem description #--------------------#
# weight = nbr of minutes for pairs of nodes corresponding to the edge
# to become friends

# first line N,M : nbr of people and nbr of pairs
# Then M lines describing each edge:
# u,v,w: u,v = indices of persons (nodes) of each edge, w = weight of edge

# output: total number of munutes to connect all people


# prims O(E + V log V) = better for dense graphs where we have (many) more edges than vertices
# if we use fibonacci heap

# kruskals O(E log V) with union find  = better for sparse graphs

#-----------------# Imports #--------------------------#

import sys
from collections import defaultdict

#---------------# Classes & Functions #--------------------------#

# kruskals:
# sort edges based on weights
# 1 start with shortest
# 2 choose next shortest edge (impossible to create cycle with only two vertices)
# 3 choose next shortest edge which wouldnt create a cycle and add
# 4 repeat 3 until we have a MST

# reads from st.in and populates graph
def populate_graph():
    f = sys.stdin.read()
    lines = f.strip().split('\n')
    nbr_people = int(lines[0].split(" ")[0])
    nbr_edges = int(lines[0].split(" ")[1])
    g = Graph(nbr_people)

    for l in lines[1:]:
        int_list = [int(ll) for ll in l.split(" ")] # std in to list of ints
        g.addEdge(int_list[0], int_list[1], int_list[2]) # add edge to graph

    return(g)


class Graph:

    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = []


    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u-1,v-1,w])


    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        #If ranks are same, then make one as root and increment
        # its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's algorithm
    def KruskalMST(self):
        time = 0
        result =[] #This will store the resultant MST

        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]

        #Step 1:  Sort all the edges in non-decreasing order of their
        # weight.  If we are not allowed to change the given graph, we
        # can create a copy of graph
        self.graph =  sorted(self.graph,key=lambda item: item[2])


        parent = [] ; rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V -1 :

            # Step 2: Pick the smallest edge and increment the index
            # for next iteration
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)

            # If including this edge does't cause cycle, include it
            # in result and increment the index of result for next edge
            if x != y:
                e = e + 1
                result.append([u,v,w])
                self.union(parent, rank, x, y)
                time = time + w # add weight to total time
            # Else discard the edge

        # print total time
        print(time)




#------------------# Script #-----------------------------#

g = populate_graph()
g.KruskalMST()
