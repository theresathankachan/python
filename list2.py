n=input("Enter a list of numbers:")
n = list(map(int, n.split()))
c=[num**2 for num in n]
print(c)
