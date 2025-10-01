def add_two():
    n1, n2 = input("Enter two numbers separated by a space: ").split()
    n2 = float(n1)
    n2 = float(n2)
    print(n1+n2)

def add_two(n1,n2):
    return n1+n2


n1, n2 = input("Enter two numbers separated by a space: ").split()
n2 = float(n1)
n2 = float(n2)

sum = add_two(n1, n2)
diff = diff_two(n1, n2)
print(f"Sum of {n1} and {n2} = {sum}")
