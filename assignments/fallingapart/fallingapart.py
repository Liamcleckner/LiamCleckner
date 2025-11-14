'''
Programmer: Liam Cleckner
Date: 11/13/25
Program: Avion - https://open.kattis.com/problems/avion
Algorithm Steps:

'''

'''
def falling_apart(piece):
    piece.sort(reverse=True)
    alice = 0
    bob = 0

    for i, val in enumerate(piece):
        if i % 2 == 0:
            alice += val
        else:
            bob += val

    return alice, bob

alice = 0
bob = 0
n = int(input())
piece = []
#piece = [input().strip() for _ in range(n)]
# print(" ".join(map(str,int)))

#piece.sort(reverse = True)
#print(" ".join(map(str,int)))

# for _ in range(n):
#     piece.append(int(input()))
n = int(input())
piece = list(map(int, input().split()))


alice, bob = falling_apart(piece)

assert len(piece) == n

print(alice)
print(bob)

'''
'''
def falling_apart(pieces):
    pieces.sort(reverse=True)
    alice = 0
    bob = 0

    for i, value in enumerate(pieces):
        if i % 2 == 0:
            alice += value
        else:
            bob += value

    return alice, bob

n = int(input())
pieces = []

for _ in range(n):
    pieces.append(int(input()))

alice, bob = falling_apart(pieces)
print(alice, bob)
'''

def falling_apart(pieces):
    pieces.sort(reverse=True)
    alice = 0
    bob = 0

    for i, value in enumerate(pieces):
        if i % 2 == 0:
            alice += value
        else:
            bob += value

    return alice, bob

n = int(input())
pieces = list(map(int, input().split()))
assert len(pieces) == n

alice, bob = falling_apart(pieces)
print(alice, bob)
