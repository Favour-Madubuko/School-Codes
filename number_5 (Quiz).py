"""def sum_n(n):
    if n <= 0:
        return 0
    else:
        return n + sum_n(n-1)
print(sum_n(0))"""

def sum_n(number):
     if n <= 0:
         print("Natural number starts from 1")
        return None
    elif isinstance(number,int) == False:
        print("Decimals not allowed")
        return None
    elif number == 1:
        return 1
    elif number > 1:
        return number + sum_n(number - 1)