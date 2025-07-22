def fib(x):
#     return fib(x-1) + fib(x-2) if x > 1 else x
    i,j = 0,1
    while x > 0:
        sum = i + j
        i = j
        j = sum
        x -= 1
    return i

for i in range(26):
    print(fib(i))
