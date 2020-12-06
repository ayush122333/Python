#import datetime
import time
import ast

def getTime():
    #return datetime.datetime.now()
    return time.asctime(time.localtime(time.time()))


d1 = {} 
d2 = {}                                             #to store the content

l1file = open("l1.txt", "r")                         ##getting names from file l1
contl1 = l1file.read()
l1 = contl1.rstrip(", ").split(",")
#print(l1)                                           #to print the names list
var1 = input("enter your name: ")

l2 = list(str.split(getTime()))
#print(l1[2])                                        #to check index of current date

# erase the data of file on new day,
#by matching date index of saved file and current date
########################################################
try:
    f1 = open(var1+".txt", "r+")
    cont = f1.read()
    l3 = cont.split()
    #print(l3[3])                                     #to check index of date
    if l2[2] != l3[3]:
        f1.truncate(0)
        f1.close()
    else:
        f1.close()
except Exception as e:
    print("")
   
########################################################

if var1 in l1:                                         #searching var1 in contl1 string
    print("you can proceed...")
    choose = int(input("press 1 to write and 2 to retrieve your information: "))       #add new feature to calculate
                                                                                       # calorie intake
    ############################################################################                                                                                   .
    if choose == 1:

        var2 = input("enter what you have eaten: ")
        d1.update({var2:getTime()})
        #print(d1)                                      #to check
        f1 = open(var1+'.txt', "a")
        f1.write(str(d1))
        print("successfully written")
        f1.close()
        l1file.close()
        
    elif choose == 2:
        try:
            info = open(var1+'.txt', "r")
            cont = info.read()
            if cont == "":
                print("nothing to show")
            print(cont)
            info.close()
            l1file.close()
        except Exception as e:
            print(e)
    else:
        print("invalid input. Exiting the application")
    ########################################################################
else:
    l1file.close()
    print("sorry you cannot use this application, should i register your name?")
    inp = input("'Y' or 'N: ")
    if inp == 'y' or inp == 'Y':
        l1file = open("l1.txt", "a")
        l1file.write(str(var1+','))
        print("registration successfull")
    elif inp == 'n' or inp == 'N':
        print("thanks for visiting.")
    else:
        print("exiting the application. Thank You for visiting")
            
               
            
        
            

            
    
