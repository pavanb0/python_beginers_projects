# creating a calculator using python function
# creat functions for basic actios
def multiplication(x, y):
    return x * y


def addition(x, y):
    return x + y


def division(x, y):
    return x / y


def substraction(x, y):
    return x - y


print("this is calculator v1.1")
print("'readme", "\n",
      " 1} give two values", "\n",
      "2} chose the arethmatic operation", "\n",
      )
ax = float(input("give the first value"))
by = float(input("give the first value"))
aret1=int(input("enter 1 for addition 0 for nothing"))
aret2=int(input("enter 2 for substraction 0 for nothing"))
aret3=int(input("enter 3 for division 0 for nothing"))
aret4=int(input("enter 4 for multiplication 0 for nothing"))
while aret1 == 1:
    res = (addition(ax, by))
    print(res,"this is your answer")
    break
while aret2 == 2:
    res = (substraction(ax, by))
    print(res,"this is your answer")
    break
while aret3 == 3:
    res = (division(ax, by))
    print(res,"this is your answer")
    break
while aret4 == 4:
    res = (multiplication(ax, by))
    print(res,"this is your answer")
    break
print("thank you for using calculator v1.1")
