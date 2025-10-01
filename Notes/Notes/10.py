print(range(10))
numbers = list(range(10))
print(f"{numbers = }")

numba = list(range(1,11))
print(f"{numba = }")

for i in range(10,0,-1):
    print(f"{i}")

name = "Stacy"
condition = ('S' in name)
print(condition)

# iterate through a string with indices
for i in range(len(name)):
    print(name[i], end=' ')
print()


while i <= 5:
    print(i, 'Hello World')
    i += 1
#Same as
for i in range(1, 6):
    print(i, "Hello World")
