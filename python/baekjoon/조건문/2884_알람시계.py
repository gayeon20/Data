a, b = map(int, input().split(" "))
c = a * 60 + b - 45
a1 = c // 60
b1 = c % 60

if a1 < 0:
    a1 += 24

print(a1, b1)
