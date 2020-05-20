#-----------------# Lab 5 - Gorillas #---------------------------------#
#-------------------# bas15fvi #------------------------------------#

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

----------------------RECURSIVE VERSION---------------------------

'''

#----------------# Imports #---------------------------------#

import sys
sys.setrecursionlimit(1500)
#import numpy as np
#----------------# Functions #------------------------------#


# funktion för att debugga i spyder som inte kan läsa stdin
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



def read_stdin():
    global Cost
    global Char_dict
    global Queries
    global Nbr_q

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





def opt2(i,j,q):
    global Opt_mat
    s = q[0]
    t = q[1]
    #if s == 'AABC':
    #    return [4, 'CBAA', 'CBA*']

    if Opt_mat[i][j] == 0:
        if i == 0 and j == 0:
            Opt_mat[i][j] = [Cost[Char_dict[s[i]]][Char_dict[t[j]]], s[i], t[j]]
        elif i == 0 and j != 0:
            opt_list = opt2(i,j-1,q)
            Opt_mat[i][j] = [-4 + opt_list[0], '*' + opt_list[1], t[j] + opt_list[2]]
        elif i != 0 and j == 0:
            opt_list = opt2(i-1,j,q)
            Opt_mat[i][j] = [-4 + opt_list[0], s[i] + opt_list[1], '*' + opt_list[2]]

        else:
            alpha = Cost[Char_dict[s[i]]][Char_dict[t[j]]]

            # ---- # nytt # -----#
            if Opt_mat[i-1][j-1] == 0:
                Opt_mat[i-1][j-1] = opt2(i-1, j-1,q)
            if Opt_mat[i][j-1] == 0:
                Opt_mat[i][j-1] = opt2(i,j-1,q)
            if Opt_mat[i-1][j] == 0:
                Opt_mat[i-1][j] = opt2(i-1,j,q)

            r1 = alpha + Opt_mat[i-1][j-1][0]
            r2 = -4 + Opt_mat[i][j-1][0]
            r3 = -4 + Opt_mat[i-1][j][0]

            if r1 >= r2 and r1 >= r3:
                Opt_mat[i][j] = [r1, s[i]+Opt_mat[i-1][j-1][1], t[j]+Opt_mat[i-1][j-1][2]]

            elif r2 > r1 and r2 >= r3:
                Opt_mat[i][j] = [r2,  '*' + Opt_mat[i][j-1][1], t[j]+Opt_mat[i][j-1][2]]

            else:
                Opt_mat[i][j] = [r3, s[i] + Opt_mat[i-1][j][1], '*' + Opt_mat[i-1][j][2]]


    return Opt_mat[i][j]



#---------------# Global variables #---------------------------#

Cost = []
Char_dict = dict()
Queries = []
formatted_strings = []
#Opt_mat = []


#----------------# Script #------------------------------------#




read_stdin()

#spyder()
out_s = ""

for n,q in enumerate(Queries):
    s_len = len(q[0])
    t_len = len(q[1])
    Opt_mat = [[0 for n in range(t_len)] for m in range(s_len)]
    s1,s2 = opt2(s_len-1, t_len-1,q)[1:]
    if n == len(Queries)-1:
        out_s = out_s + s1[::-1] + " " + s2[::-1]
    else:
        out_s = out_s + s1[::-1] + " " + s2[::-1] + '\n'
print(out_s)
