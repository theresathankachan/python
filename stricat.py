str=input("Enter a string:")
l=len(str)
if(l>2):
    s=str[0:2:]+str[-2:]
    print("resultant string=",s)
elif(l==2):
    s=str+str
    print(s)
else:
    print('')
        
