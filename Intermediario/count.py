from itertools import count

c1 = count(start=8, step=8)
for i in c1:
    if i >= 100:
        break
    print(i)