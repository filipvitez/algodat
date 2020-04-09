#----------------# imports #---------------------#
import sys
from collections import defaultdict
from collections import deque
import time


# -------------------# functions #----------------------#

#should be n^2 but seems a lot slower, does not break when we have found our target
def shortest_path2(graph, start,end):
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = dist[at]+[next]
                #dist[next] = [dist[at], next]
                q.append(next)
    return dist.get(end)


# uglier but quicker. (0(n+m))
def shortest_path3(graph,start,end):
    visited = {start: ""} # keep track of visited (and their prev node)
    q = deque([start])

    flag = 0 #to break out of both loops for cases we have found our target


    if start == end:
        return 0

    # n+m at worst (when there is no path between start/end or if end is the last)
    while q: # keep going until we either find our target or run out of nodes
        s = q.popleft()
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited[neighbour] = s
                q.append(neighbour)
                # we have found our target
                if neighbour == end:
                    flag = 1
                    break
        # double break to escape while-loop as well
        if flag:
            break

    # n at worst (when nodes are as far from each other as possible)
    if flag:
        i = 0
        pos = neighbour
        while pos != "":
            pos = visited[pos]
            i = i+1
        return i-1
    else:
        return "Impossible"



#---------------# Start of script #------------------------#

# TODO: put this in a separate function
# Read from standard in
f = sys.stdin.read()
lines = f.strip().split('\n')
words = int(lines[0].split(" ")[0])

# Special type of dict that works better when values are lists
dfdict = defaultdict(list)

# n^2. Could be done in linear time by taking max amount of possible neighbors
# into account. (permutations of 5-letter words with the last 4 letters having
# picked from a collection of 4)
for l in lines[1:words+1]:
    dfdict[l] = list() # create key for each word initialized with empty list
    templ = [c for c in l[1:]] # only look at the last four letters + reformat as vector
    for ll in lines[1:words+1]: # nested loop to connect each word to all others
        if l != ll: # cannot connect to itself
            templl = [c for c in ll] # reformat as vector (so that we can use count())
            if (0 not in [templ.count(c) <= templl.count(c) for c in templ[-4:]]):
                dfdict[l].append(ll) #for a normal dict, this did not work as wanted

# convert to normal dict
graph = dict(dfdict)

# time algo
#import time
#t0 = time.time()

# calc shortest path between all words of graph
for seq in lines[words+1:]:
    ret = shortest_path3(graph, seq.split(" ")[0], seq.split(" ")[1])
    print(ret)

# time algo
#t1 = time.time()
#print(t1-t0)
