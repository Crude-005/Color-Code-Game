#welcone to the colour combo game
import random
print ("WELCOME TO THE COLOUR COMBO GAME")
print ("COLOUR CODES: \n A=RED \n B=BLUE \n C=GREEN \n D=YELLOW \n E=PINK \n F=ORANGE")
c=0
set_len=4
set_chances=10
set_variables=6
while c==0:
    print ("Enter \n [0] to exit \n [1] to start \n [2] for rules \n [3] for settings")
    mod=input(": ")
    if mod=="1":
        print ("Enter \n [0] to exit \n [1] to start with a random set \n [2] to start with a custom set ")
        _mod1=input(": ")
        if _mod1=="0":
            continue
        elif _mod1=="1":
            _ori = ""
            for i in range(0,set_len):
                _randomint= random.randint(0,set_variables-1)
                colourlist= ["A","B","C","D","E","F","G","H","I","J",
                             "K","L","M","N","O","P",
                             "Q","R","S","T","U","V","W","X","Y","Z"]
                _ori += colourlist[_randomint]
                continue
            _ch=1 #chance
            l_ori=list(_ori)
            while _ch <= set_chances+1 :
                if _ch == set_chances+1 :
                    print ("DEFEAT \n The original set was ", _ori, "\n Better luck next time")
                    _ch+=1
                    continue
                else:
                    print ("Enter the set (expected length",set_len ,")", _ch )
                    n=input(":")
                    n=n.upper()
                    l_n=list(n)
                    if n== "REVEAL":
                        print (f"The correct answer is {_ori}")
                        break
                    if len(n) == len(_ori):
                        r=0
                        w=0
                        for i in range (0,set_len):
                            if n[i]== _ori[i]:
                                r+=1
                        for i in l_ori:
                            if l_n.count(i)>0:
                                l_n.remove(i)
                                w+=1
                        w -= r
                        if r == set_len:
                            print ("BOOYAH! You made it in" ,_ch,"chances" )
                            break
                        else:
                            print ("R= ", r, "W= ", w)
                            _ch+=1
                            continue
                        continue
                    else:
                        print ("Invalid input")
                        continue
                    continue
                continue
            continue
        elif _mod1=="2":
            _ch=1 #chance
            _ori = input("Enter a set: " ) #original set
            _ori = _ori.upper()
            l_ori=list(_ori)
            if len(_ori) == set_len:
                print (".\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n")
                print (".\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n")
                print (".\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n")
                print (".\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n")
                while _ch <= set_chances+1 :
                    if _ch == set_chances+1:
                        print ("DEFEAT \n The original set was ", _ori, "\n Better luck next time")
                        _ch+=1
                        continue
                    else:
                        print ("Enter the set", _ch )
                        n=input(":")
                        n=n.upper()
                        l_n=list(n)
                        if n== "reveal":
                            print (f"The correct answer is {_ori}")
                            break
                        if len(n) == len(_ori):
                            r=0
                            w=0
                            for i in range (0,set_len):
                                if n[i]== _ori[i]:
                                    r+=1
                            for i in l_ori:
                                if l_n.count(i)>0:
                                    l_n.remove(i)
                                    w+=1
                            w -= r
                            if r == set_len:
                                print ("BOOYAH! You made it in" ,_ch,"chances" )
                                break
                            else:
                                print ("R= ", r, "W= ", w)
                                _ch+=1
                                continue
                            continue
                        else:
                            print ("Invalid input")
                            continue
                        continue
                    continue
                continue
            else:
                print ("Invalid input \n Expected length:",set_len)
            continue
        else:
            print ("Invalid input")
            continue
        continue
    elif mod=="0" :
        c+=1
        continue
    elif mod=="3":
        d=0
        while d==0:
            print ("Enter \n [0] to exit"
                   "\n [1] to change length"
                   "\n [2] to change number of chances"
                   "\n [3] to change number of variables"
                   "\n [4] for default settings")
            _mod3=input(": ")        
            if _mod3 == "0":
                d+=1
                continue
            elif _mod3== "1":
                n_set_len=int(input("Enter the new length for set: "))
                set_len = n_set_len
                continue
            elif _mod3=="2":
                n_set_chances = int(input("Enter the new chances: "))
                set_chances= n_set_chances
                continue
            elif _mod3=="4":
                set_len=4
                set_chances=10
                set_variables=6
                continue
            elif _mod3=="3":
                n_set_variables=int(input("Enter the new number of variables: "))
                if n_set_variables >=26:
                    n_set_variables = 26
                set_variables = n_set_variables               
            else:
                print ("Invalid input")
                continue
            continue
        continue
    elif mod=="2":
        print ("Rules not decided yet")
        continue
    else:
        print ("Invalid input")
        continue
    continue

print ("Thank you for playing")
print ("THE END")
