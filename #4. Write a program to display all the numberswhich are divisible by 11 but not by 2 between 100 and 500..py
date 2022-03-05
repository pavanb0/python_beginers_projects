#4. Write a program to display all the numberswhich are divisible by 11 but not by 2 between 100 and 500.
#"""but not by 2 between 100 and 500.""" not understand this part of the question but considering
low = int(input("lower value"))
up = int(input("upper value"))
#(case 1) divisible by 1
carry=0
qarry=0
for i in range(low,up+1):
    if i<1:
        break
    if (i%11)==0:
        vol=carry+i
        print(vol)
print("1st value invalid try value greater than 0")
for i in range(low,up+1):
    if i<1:
        break
    if (i%2)==0:
        l=qarry+i
        print(l)
print("2nd value invalid try value greater than 0")






