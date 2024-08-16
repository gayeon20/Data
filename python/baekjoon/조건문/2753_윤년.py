a = int(input())
condition1 = a % 4 == 0
condition2 = a % 100 != 0 or a % 400 == 0

if condition1 and condition2:
    print("1")
else:
    print("0")

# if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
#     print("1")
# else:
#     print("0")
