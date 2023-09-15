b = int(input())
t = int(input())

lb2 = 160 - b
lt2 = 160 - t

lb1 = 160 - lb2
lt1 = 160 - lt2

if lb1 > lt2 and lt1 > lb2:
    print(1)
elif lb2 > lt1 and lt2 > lb1:
    print(2)
else:
    print(0)
