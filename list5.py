n = input("Enter a list of numbers: ")
n = list(map(int, n.split()))
p=[num for num in n if num%2]
print(p)
