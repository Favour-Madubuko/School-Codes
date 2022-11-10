'''def do_n(s,n):
    if n<= 0:
        return
    print(s)
    do_n(s, n-1)
do_n("hello",3)

def do_n2(s,n):
    for i in range(1,n):
        if n <= 0:
            return
        print(s,i)
do_n2("hello",4)'''
def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result
factorial(4)

        
        
        