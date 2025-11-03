'''
Programmer: Liam Cleckner
Class: CS110
Program: Kattis problem - https://open.kattis.com/problems/hardwoodspecies
Algorithm:
    input lines "trees" into a list
        use for line in sys.stdin:
'''



import sys

species = sys.stdin.readlines() # return a list of lines until BOF
print(species[0].strip())

print(species)


species = []
for line in sys.stdin:
    species.append(line)

print(species[0])
