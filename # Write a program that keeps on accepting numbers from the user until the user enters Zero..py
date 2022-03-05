# Write a program that keeps on accepting numbers from the user until the user enters Zero.
# Display the sum and average of all the numbers
#hard work payed off
cout = 0
num = 0
while (num == 0):
    anum = input("enter list of number if  '0' you get sum")
    i = int(anum)

    if i == 0:
        break
    else:
         cout=cout+i
         a=str(cout)
         divi=len(a)
print("your sum is",cout//divi,"thank you")
