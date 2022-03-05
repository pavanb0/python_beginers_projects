import random  #its pythons liabrary to chose for gusseing random
namo=int(input("how many time you want to toss coin")) #take input from user
print("if you toss coin over",namo,"times")
def perce(x,y): #creat function for finding the percentage
    x=x/namo * 100
    y=y/namo * 100
    print("chances of heads",x,"and chances of tails",y)
    return True
count=0 #universal counter initialize by zero
count1=0 #universal counter initialize by zero
v = ("heads", "tails") #creating a tuple with two items
try: # exeption handling or error handling
  for i in range(1,namo+1): #going 1 to user defined value
      if i<=namo+1: #given condition
          result = random.choice(v) #main twist over here : python liabrary random tring to guess randomly if its H or T
          if result=="heads":
              count=count+1
          elif result=="tails":
              count1 = count1 + 1

except Exception:
    print("something went wrong" )
k=perce(count, count1) # passing result function
