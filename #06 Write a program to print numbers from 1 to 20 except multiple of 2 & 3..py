#06 Write a program to print numbers from 1 to 20 except multiple of 2 & 3.
low = int(input("lower value"))
up = int(input("upper value"))
#not including multiple of 2,3 like 2,4,6,8 and 3,6,9
flag=0
for a in range(low,up+1):
    if a % 2 != 0:
        if a % 3 != 0:
            print(a)