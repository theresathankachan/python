#Accept a list of integers from user. For all values above 100 store the string ‘Over’ in the specific position.
l=list(map(int,input("enter numbers:").split()))
for i in l:
       if i>100:
           l[l.index(i)]='OVER'
print(*l,sep=',')
