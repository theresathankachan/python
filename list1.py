n = input("Enter a list of numbers:")
n = list(map(int, n.split()))
count=[num for num in n if num>0]
print(count)
