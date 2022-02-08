#Write a program to generate all factors of a given number.
n=int(input("Enter number:"))
i=1
while i<=n:
    if n%i==0:
        print('factors=',i)
    i=i+1
