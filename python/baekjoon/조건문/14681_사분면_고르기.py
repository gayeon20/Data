a = int(input())
b = int(input())
con1 = a > 0 and b > 0
con2 = a < 0 and b > 0
con3 = a < 0 and b < 0
con4 = a > 0 and b < 0
if con1:
    print("1")
elif con2:
    print("2")
elif con3:
    print("3")
elif con4:
    print("4")
