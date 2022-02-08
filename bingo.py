str=input('enter a string:')
temp=0
c=0
word=str.split()
for w in word:
 if len(w)>temp:
          temp=len(w)
 elif temp==len(w):
          c=1
else :
          c=2
print("largest word length:",temp)
if c==1:
    print('Bingo')




















          
