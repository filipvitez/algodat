# --------# Imports # ---------------#
import sys
from time import time
import collections

# ---------- # Read & sort in-files #---------------------#

def inv_list(l):
    out = [0]*(N+1)
    for i in range(N):
        out[l[i]] = i
    return out



f = sys.stdin.read()

lines = f.strip().split('\n')
N = int(lines[0])


women = [[] for _ in range(N+1)]
men = [[] for _ in range(N+1)]
allinp = [int(x) for line in lines[1:] for x in line.split()]
for person in range(2*N):
    person_inp = allinp[person*(N+1):(person+1)*(N+1)]
    person_id = person_inp[0]
    person_inv_pref_list = inv_list(person_inp[1:])
    if women[person_id]: men[person_id] = person_inv_pref_list
    else: women[person_id] = person_inv_pref_list


# Formatting input to work for my algo
# (I previoiusly imported the data in another way and the algo is built upon that)

men = men[1:]
women = women[1:]

men = [m[1:] for m in men]
women = [w[1:] for w in women]

men = [[x+1 for x in mm] for mm in men]
women = [[x+1 for x in ww] for ww in women]


nbr_women = N

# Change men list to not have position-format (se föreläsning 1.6)
# I.e change from [2 3 4 1] -> [4 1 2 3]

new_men = [None]*N

for j,m in enumerate(men):
    tlist = [None]*N
    for i, mm in enumerate(m):
        tlist[mm-1] = i+1
    new_men[j] = tlist


men = new_men
del(new_men)

# Uncomment to time algo
#print("starting algo")
#t0 = time()

#--------------# Start of Algo #------------------------#

men_index = [m for m in range(0, nbr_women)]
women_index = [w for w in range(0, nbr_women)]

# key = woman index
# value = index of man paired with woman
pairs = dict()

while len(men_index) != 0:
    # kvinna som mannen vill ha mest, givet att hon e valid
    preferred_woman = men[men_index[0]][0]

    # kvinna är friad till så ta bort från mannens preferenslista
    men[men_index[0]].pop(0)

    # Kvinna har ingen partner
    if pairs.get(preferred_woman) == None:
        pairs[preferred_woman] = men_index[0] # en för lite
        men_index.pop(0)
    # Kvinna har partner men gillar nya mannen mer
    elif women[preferred_woman-1][men_index[0]] < women[preferred_woman-1][pairs.get(preferred_woman)]:
        men_index.append(pairs.get(preferred_woman))
        pairs[preferred_woman] = men_index[0]
        men_index.pop(0)
    # Kvinna har partner och gillar denne mer
    else:
        continue



# Sort dict based on key
sorted_pairs = collections.OrderedDict(sorted(pairs.items()))


# Output
for k,v in sorted_pairs.items():
    print(v+1)


# Uncomment to time algo
#t2 = time()
#print(t2-t0)



# ----------------------------------------------_#
# Hade denna sortering & inläsning tidigare innan jag såg att jag kunde kopiera lab-skaparens

# f = sys.stdin.read()
#
# f = f.replace(" ", "").splitlines()
# men = []
# women = []
# taken_mindexes = []
# taken_windexes = []
# nbr_women = int(f[0])
# ordered_women = [None]*(nbr_women)
# ordered_men = [None]*(nbr_women)
#
# #try:
#
# for ff in f[1:]:
#     if not ff[0] in taken_windexes:
#         taken_windexes.append(ff[0])
#         women.append(ff)
#     else:
#         taken_mindexes.append(ff[0])
#         men.append(ff)
#
# # order women-pref based on index of men
# for k,w in enumerate(women):
#     templist = [int(w[0])]*(nbr_women+1)
#     for i, ww in enumerate(w[1:]):
#         templist[int(ww)] = i+1
#     ordered_women[k] = templist
#
# women = sorted(ordered_women, key=lambda x: x[0])
# del(ordered_women)
#
# #print(women)
#
# for l, m in enumerate(men):
#     templist = [None]*(nbr_women+1)
#     for j, mm in enumerate(m):
#         #print(j)
#         templist[j] = int(mm)
#     ordered_men[l] = templist
#
#
# men = sorted(ordered_men, key=lambda x: x[0])
# del(ordered_men)
#
# men = [x[1:] for x in men]
# women = [x[1:] for x in women]
