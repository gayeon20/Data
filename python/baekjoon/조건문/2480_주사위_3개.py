a, b, c = map(int, input().split(" "))
aa = max(a, b, c)
cond1 = (a == b == c)
cond2 = (a == b)
cond3 = (a == c)
cond4 = (b == c)

if cond1:
    print(10000 + a * 1000)
elif cond2 or cond3:
    print(1000 + a * 100)
elif cond4:
    print(1000 + b * 100)
else:
    print(aa * 100)
