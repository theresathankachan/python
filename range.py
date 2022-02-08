#Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square.
r1=int(input("Enter range:"))
r2=int(input("Enter range:"))
for i in range(r1,r2,1):

   for j in range(1,100,1):

       if i == j*j:

           string = str(i)

           if int(string[0])%2 == 0 and int(string[1])%2 == 0 and int(string[2])%2 == 0 and int(string[3])%2 == 0:

               print(i)
