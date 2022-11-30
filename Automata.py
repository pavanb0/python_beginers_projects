arr = ["a"]
global flag1, flag2

def check(arr):
    flag1,flag2=False,False
    try:    
        for i in range(len(arr)):
            if arr[i] == "a":
                if arr[i+1] == "b":
                    if arr[i+2] == "a":
                        if arr[i+3] == "b":
                            flag1 = True
    except IndexError:
        flag2 = True

    if flag1 and flag2:
        return True
    else:
        return False    
while True:
    ins = str(input("Enter a string: ")) 
    if check(ins):
        print("😊")   
    else:
        print("😢")
        break
