def recursiva(start=0, end=4):
    if start >= end:
        return end
    
    start += 1
    return recursiva(start, end)

print(recursiva())

num = input('Digite um numero para ver o seu factorial: ')
num = int(num)

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

print(fact(num))