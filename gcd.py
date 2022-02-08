#GCD of 2 numbers
m=int(input("Enter number:"))
n=int(input("Enter number:"))
i=1
while i<=m and i<=n:
    if m%i==0 and n%i==0:
        gc=i
    i=i+1
print('GCD=',gc)
