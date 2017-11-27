def fib(n):
    if n==0:
        return []
    elif n==1:
        fibList=[0]
        return fibList

    fibList=[0,1]
    for x in range(n-2):
        nextNum=fibList[-1]+fibList[-2]
        fibList.append(fibList[-1]+fibList[-2])
    return fibList


"""a=fib(12)
for elem in a:
    if elem<5:
        print elem

print filter(lambda x: x<5,a)

number=int(raw_input("enter a number to only print less then"))

print filter(lambda x:x<number,a)
"""