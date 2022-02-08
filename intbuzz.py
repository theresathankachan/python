#program to print numbers from 1 to 20. For every multiple of 3,print ‘Fizz’, for every multiple of 5, print ‘Buzz’ and for every multiple of both 3 and 5 print ‘FizzBuzz’, instead of the original number.for i in range(1,21):
    
    if i%5==0 and i%3==0:
        print("fizzbuzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")
    else:
        print(i)
