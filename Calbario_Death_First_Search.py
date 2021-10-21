#-------------------------------------------------------------------------------
# CS142 Assignment 2: Death First Search - Episode 1
# A solution to the activity Death First Search - Episode 1 from Codin Game.
#
# Rica Bernadine Calbario
# CS142 - G
#-------------------------------------------------------------------------------

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def checkNodes(si, gates):
    global links
    for g in gates:
        if g in links[si]:
            return [si, g]
    for g in gates:
        if len(links[g]) > 0:
            return [g, links[g][0]]
    return [0, 0]

def linkBreaker(a1, a2):
    global links
    links[a1].remove(a2)
    links[a2].remove(a1)

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

gates = []
links = {}

for i in range(l):     # defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    links.setdefault(n1, []).append(n2)
    links.setdefault(n2, []).append(n1)

for i in range(e):
    ei = int(input())  # the index of a gateway node
    gates.append(ei)

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    a1, a2 = checkNodes(si, gates)
    linkBreaker(a1, a2)
    print("{0} {1}".format(a1,a2))

# Reference: https://github.com/vadim-job-hg/Codingame/blob/master/MEDIUM/SKYNET%20REVOLUTION%20-%20EPISODE%201/python/skynet-revolution-episode-1.py
