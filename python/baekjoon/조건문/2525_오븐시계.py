a, b = map(int, input().split(" "))
c = int(input())
aa = a * 60 + b + c
a1 = aa // 60
b1 = aa % 60

if a1 >= 24:
    a1 = a1 - 24

print(a1, b1)
