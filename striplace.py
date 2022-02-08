s=input("Enter a string:")
n=s.find('not')
b=s.find('bad')
if b > n:
    s=s.replace(s[n:(b+3)],'good')
    print(s)
