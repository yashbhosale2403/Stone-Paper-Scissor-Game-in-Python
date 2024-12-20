"""
-1 stone
0 paper
1 scissor

"""

import random

print("\t lets  play stone paper seissor \n\t\n\t now select stone or paper or scissor")

computer=random.choice([-1,0,1])
computerdict={-1:"stone",0:"paper",1:"scissor"}
reversedict=computerdict[computer]
yourstr=input("\nenter what is your choise = ")
yourdict={"stone":-1,"paper":0,"scissor":1}
you=yourdict[yourstr]

print(f"computer choose = {reversedict}")

if(computer==you):
    print("\n\tthis match is tie")
else:    
    if(computer==-1 and you==0):
        print("\n\tyou win")
    elif(computer==-1 and you==1):
        print("\n\tcomputer win")
    elif(computer==0 and you==-1):
        print("\n\tcomputer win")
    elif(computer==0 and you==1):
        print("\n\tyou win")
    elif(computer==1 and you==-1):
        print("\n\tyou win") 
    elif(computer==1 and you==0):
        print("\n\tcomputer win")
    else:    
        print("\n\tsomething is wrong")