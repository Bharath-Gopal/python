#Fibonacci Series
def fib(n):
    print ("Fibonacci series for first ",n," terms : ")
    first = 1
    second = 1
    count = 2
    print (first,end=' ')
    print (second,end=' ')
    while count!=n :
        third = first+second 
        first = second 
        second = third
        count += 1
        print (third,end=' ')
    print('\n')

fib(5)
fib(10)