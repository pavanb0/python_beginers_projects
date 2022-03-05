#this block of code test your typing speed
import re
import time
from operator import length_hint
text="encompasses the social behavior and norms found in human societies, as well as the knowledge, beliefs, arts, laws, customs"
split_text=re.split("\s",text)
def second_to_minute(sec):
    minutes=sec/60
    return minutes;
def wpmn(words,times):
    wpms=words/times
    return wpms;
def wpm (host,guest,length):
     flag=0
     while True:
         for i in range(0,length):
             if host[i] in guest:
                 print("flag")
                 flag = flag + 1
                 print(flag)
             else:

                 return flag;
         break
print("welcome to 'type o metre' check your typing speed and accurecy")
response=str(input("would you like to begine with thise test:/|\: (yes/no)"))
response.lower()
if 1==1:
    print("welcome","\n","*brefly look at the paraghph*")
    print("-------------------------------------------------------------------------")
    print("we will throw 1 line at time ready!!!!!!!!!")
    print("-------------------------------------------------------------------------")
    res = str(input(" will start ready (yes/no)"))
    res.lower()
    if 1==1:
        print(text)
        go=time.time()
        user_in=str(input(""))
        end=time.time()
        time_that_usertook=(end-go)
        po=re.split("\s",user_in)
        po_length = len(po)
        returnvalue=(wpm(split_text,po,po_length))
        wpmf=(second_to_minute(time_that_usertook))
        speed=wpmn(returnvalue,wpmf)
        print(time_that_usertook,po,"you type around",speed,"per minutes")
        print(len(split_text))







