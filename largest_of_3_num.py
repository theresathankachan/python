#largest of three numbers
a = int(input('Enter first integer : '))
b = int(input('Enter second integer : '))
c = int(input('Enter third integer : '))
if (a>b and a>c):
    print('Largest - ',a)
    elif (b>c):
        print('Largest - ',b)
        else:
            print('Largest - ',c)
