#-----------------# Lab 5 - Gorillas #---------------------------------#
#-------------------# Filip & Mikael #------------------------------------#

#-----------# Problem description #---------------------------#

'''
Align strings using a Dynamic Programming-algorithm

Input:
1st line: A number of space-separated characters, c_1,...c_k (that will be
used in the strings)
k lines: Space-separated integer where j-th nbr on the i-th row is the cost of
aligning c_i and c_j
nd line: One line with integer Q(1≤Q≤10) => nbr of queries to solve
Q lines: each describing one query


------------------ ITERATIVE VERSION ------------------------------

'''

#----------------# Imports #---------------------------------#

import sys

#----------------# Functions #------------------------------#


# function to debug using spyder (where reading from st in is impossible)
def spyder():
    global Cost
    global Char_dict
    global Queries
    global Nbr_q
    f = '''
    A B C
2 0 -1
0 3 1
-1 1 3
2
AABC ABC
ABA ACA
    '''
    lines = f.strip().split('\n')
    characters = lines[0].split(" ")

    #Char_dict = dict()
    for i, c in enumerate(characters):
        Char_dict[c] = i

    #return char_dict

    nbr_c = len(characters)
    Cost = [0]*nbr_c
    for i in range(nbr_c):
        temp = lines[i+1].split(" ")
        Cost[i] = [int(t) for t in temp]

    Nbr_q = int(lines[nbr_c+1])
    Queries = [0]*Nbr_q
    for i in range(Nbr_q):
        s1,s2 = lines[2 + nbr_c + i].split(" ")
        Queries[i] = [s1,s2]


# Read from std.in and assign global vars
def read_stdin():
    global Cost
    global Char_dict
    global Queries
    #global Nbr_q

    # read from std in
    f = sys.stdin.read()
    lines = f.strip().split('\n')
    characters = lines[0].split(" ")

    # populate Character-number-dict
    for i, c in enumerate(characters):
        Char_dict[c] = i

    # populate Cost-matrix
    nbr_c = len(characters)
    Cost = [0]*nbr_c
    for i in range(nbr_c):
        temp = lines[i+1].split(" ")
        Cost[i] = [int(t) for t in temp]

    # populate Queries-list
    Nbr_q = int(lines[nbr_c+1])
    Queries = [0]*Nbr_q
    for i in range(Nbr_q):
        s1,s2 = lines[2 + nbr_c + i].split(" ")
        Queries[i] = [s1,s2]


# Populate opt-matrix for query q
def build_opt_mat(q):
    global Opt_mat
    s = q[0]
    t = q[1]
    Opt_mat = [[0 for n in range(len(t)+1)] for m in range(len(s)+1)]

    #
    for i in range(len(s)+1):
        Opt_mat[i][0] = i*(-4)
    for j in range(len(t)+1):
        Opt_mat[0][j] = j*(-4)
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            match = Cost[Char_dict[s[i-1]]][Char_dict[t[j-1]]] + Opt_mat[i-1][j-1]
            m1 = -4 + Opt_mat[i-1][j]
            m2 = -4 + Opt_mat[i][j-1]
            Opt_mat[i][j] = max(match,m1,m2)


# Finds and returns optimal sequence alignment (using iterative method)
def opt_iterative(q):

    s = q[0]
    t = q[1]
    i = len(s)
    j = len(t)

    align1 = ""
    align2 = ""

    while  i > 0 and j > 0:
        current = Opt_mat[i][j]
        diag = Opt_mat[i-1][j-1]
        up = Opt_mat[i][j-1]
        down = Opt_mat[i-1][j]
        alpha = Cost[Char_dict[s[i-1]]][Char_dict[t[j-1]]]

        # if we have come from a match
        if current == diag + alpha:
            align1 += s[i-1]
            align2 += t[j-1]
            i -= 1
            j -= 1
        # if we have come from a '*' in the first seq
        elif current == up - 4:
            align1 += '*'
            align2 += t[j-1]
            j -= 1
        # if we have come from a '*' in the second seq
        elif current == down - 4:
            align1 += s[i-1]
            align2 += '*'
            i -= 1

    while j>0:
        align1 += '*'
        align2 += t[j-1]
        j -= 1
    while i>0:
        align1 += s[i-1]
        align2 += '*'
        i -= 1

    align1 = align1[::-1]
    align2 = align2[::-1]

    return align1 + " " + align2








#---------------# Global variables #---------------------------#

Cost = []
Char_dict = dict()
Queries = []



#----------------# Script #------------------------------------#

read_stdin()
#spyder()

for q in Queries:
    build_opt_mat(q)
    print(opt_iterative(q))
