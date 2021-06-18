#list for store latter of user input 
L1 = []
#line for taking input from user
name =input("enter your name:")
#find the lenght of word taken by the user
length = len(name)
#for loop for add all latters of user word in list L1
sl = 0
for sl in range(length):
    sl +=1
    L1.insert(sl, name[(sl-1):(sl)])
i = 0
#function for writting A in star formation
def a(): 
    for i in range(3):
        i += 1
        print (" "*(8-i) + "*"*2 + " "*2*(i-1) + "*"*2)
    print(" "*4, end="")
    print("*"*10)
    print(" "*3, end="")
    print("*"*12)
    for i in range(3):
        i += 1
        print (" "*(3-i) + "*"*2 + " "*2*(4+i) + "*"*2)


#function for writting B in star formation
def b():
    for i in range(2):
        i += 1
        print ("*"*2 + " "*4*(i-1) + "*"*(7-2*i))
    for i in range(2):
        i += 1
        print ("*"*2 + " "*4*(2-i) + "*"*(1+i*2))
    for i in range(2):
        i += 1
        print ("*"*2 + " "*4*(i-1) + "*"*(7-2*i))
    for i in range(2):
        i += 1
        print ("*"*2 + " "*4*(2-i) + "*"*(1+i*2))


#function for writting C in star formation
def c():
    for i in range(2):
        i += 1
        print (" "*(5-i*2) + "*"*(4+i*2))
    for i in range(4):
        i += 1
        print ("*"*2)
    for i in range(2):
        i += 1
        print (" "*(i*2-1) + "*"*(10-i*2))


#function for writting D in star formation
def d():
    for i in range(2):
        i += 1
        print ("*"*(7+2*(i-1)))
    for i in range(4):
        i += 1
        print ("*"*3 + " "*4 + "*"*3)
    for i in range(2):
        i += 1
        print ("*"*(9-2*(i-1)))


#function for writting E in star formation
def e():
    for i in range(2):
        print("*"*10)
    print("*"*3)
    for i in range(2):
        print("*"*10)
    print("*"*3)
    for i in range(2):
        print("*"*10)


#function for writting F in star formation
def f():
    for i in range(2):
        print("*"*10)
    print("*"*3)
    for i in range(2):
        print("*"*10)
    for i in range(3):
        print("*"*3)


#function for writting G in star formation
def g():
    for i in range(2):
        i += 1
        print(" "*(3-2*(i-1)) + "*"*(6+4*(i-1)))
    for i in range(2):
        i += 1
        print("*"*2)
    print("*"*2 + " "*4 + "*"*6)
    print("*"*2 + " "*8 + "*"*2)
    for i in range(2):
        i += 1
        print(" "*(1+2*(i-1)) + "*"*(10-4*(i-1)))


#function for writting H in star formation
def h():
    for i in range(4):
        print("*"*2 + " "*6 + "*"*2)
    for i in range(2):
        print("*"*10)
    for i in range(4):
        print("*"*2 + " "*6 + "*"*2)


#function for writting I in star formation
def I():
    for i in range(2):
        print("*"*13)
    for i in range(6):
        print(" "*5 + "*"*3)
    for i in range(2):
        print("*"*13)

#function for writting J in star formation
def j():
    for i in range(2):
        print("*"*10)
    for i in range(2):
        print(" "*8 + "*"*2)
    for i in range(2):
        print("*"*2 + " "*6 + "*"*2)
    for i in range(2):
        i += 1
        print(" "*i + "*"*(8-2*i))


#function for writting K in star formation
def k():
    for i in range(4):
        i += 1
        print("*"*2 + " "*(8-i*2-1) + "*"*3)
    for i in range(4):
        i += 1
        print("*"*2 + " "*(2*(i-1)-1) + "*"*3)


#function for writting L in star formation
def l():
    for i in range(6):
        i += 1
        print("*"*2)
    for i in range(2):
        print("*"*12)


#function for writting M in star formation
def m():
    for i in range(4):
        print("*"*2 + " "*(i) + "*"*2 + " "*(6-2*i) + "*"*2 + " "*(i) + "*"*2)
    for i in range(4):
        print("*"*2 + " "*10 + "*"*2)   


#function for writting N in star formation
def n():
    for i in range(8):
        print("*"*2 + " "*(i) + "*"*2 + " "*(8-i) + "*"*2)


#function for writting O in star formation
def o():
    for i in range(2):
        i += 1
        print(" "*(3-2*(i-1)) + "*"*(6+4*(i-1)))
    for i in range(4):
        i += 1
        print("*"*2 + " "*8 + "*"*2)
    for i in range(2):
        i += 1
        print(" "*(1+2*(i-1)) + "*"*(10-4*(i-1)))


#function for writting P in star formation
def p():
    for i in range(2):
        i += 1
        print ("*"*2 + " "*4*(i-1) + "*"*(7-2*i))
    for i in range(2):
        i += 1
        print ("*"*2 + " "*4*(2-i) + "*"*(1+i*2))
    for i in range(4):
        i += 1
        print("*"*2)


#function for writting Q in star formation
def q():
    for i in range(2):
        i += 1
        print(" "*(3-2*(i-1)) + "*"*(6+4*(i-1)))
    for i in range(6):
        print("*"*2 + " "*(i) + "*"*2 + " "*(6-i) + "*"*2)
    for i in range(2):
        i += 1
        print(" "*(1+2*(i-1)) + "*"*(10-4*(i-1)))


#function for writting R in star formation
def r():
    for i in range(2):
        i += 1
        print ("*"*2 + " "*4*(i-1) + "*"*(7-2*i))
    for i in range(2):
        i += 1
        print ("*"*2 + " "*4*(2-i) + "*"*(1+i*2))
    for i in range(4):
        i += 1
        print("*"*2 + " "*(2*(i-1)-1) + "*"*3)


#function for writting S in star formation
def s():
    print(" " + "*"*8)
    for i in range(2):
        i += 1
        print(" "*(i-1) + "*"*(4-i) + " "*(4+i) + "*"*(3-i))
    for i in range(2):
        i += 1
        print(" "*(2*i+1) + "*"*2)
    for i in range(2):
        i += 1
        print("*"*i + " "*(7-i) + "*"*(1+i))
    print(" " + "*"*8)


#function for writting T in star formation
def t():
    for i in range(2):
        print("*"*13)
    for i in range(6):
        print(" "*5 + "*"*3)


#function for writting U in star formation
def u():
    for i in range(6):
        print("*"*2 + " "*8 + "*"*2)
    for i in range(2):
        i += 1
        print(" "*i + "*"*(12-i*2))


#function for writting V in star formation
def v():
    for i in range(8):
        print(" "*(i) + "*"*2 + " "*(14-2*i) + "*"*2)


#function for writting w in star formation
def w():
    for i in range(4):
        print("*"*2 + " "*10 + "*"*2)
    for i in range(4):
        print("*"*2 + " "*(3-i) + "*"*2 + " "*(2*(i)) + "*"*2 + " "*(3-i) + "*"*2 )

#function for writting X in star formation
def x():
    for i in range(4):
        print(" "*(i) + "*"*2 + " "*(7-2*i) + "*"*2)
    for i in range(4):
        print(" "*(3-i) + "*"*2 + " "*(2*i+1) + "*"*2)


#function for writting Y in star formation
def y():
    for i in range(4):
        print(" "*(i) + "*"*2 + " "*(7-2*i) + "*"*2)
    for i in range(4):
        print(" "*(5-i) + "*"*2)        


#function for writting Z in star formation
def z():
    for i in range(2):
        print("*"*13)
    for i in range(6):
        print(" "*(10-i*2) + "*"*3)
    for i in range(2):
        print("*"*13)

# name = g()
# print(name)

def func_iter():       
    if check == "a" or check == "A":
        myfunc = a()
    elif check == "b" or check == "B":
        myfunc = b()
    elif check == "c" or check == "C":
        myfunc = c()
    elif check == "d" or check == "D":
        myfunc = d()
    elif check == "e" or check == "E":
        myfunc = e()
    elif check == "f" or check == "F":
        myfunc = f()
    elif check == "g" or check == "G":
        myfunc = g()
    elif check == "h" or check == "H":
        myfunc = h()
    elif check == "i" or check == "I":
        myfunc = I()
    elif check == "j" or check == "J":
        myfunc = j()
    elif check == "k" or check == "K":
        myfunc = k()
    elif check == "l" or check == "L":
        myfunc = l()
    elif check == "m" or check == "M":
        myfunc = m()
    elif check == "n" or check == "N":
        myfunc = n()
    elif check == "o" or check == "O":
        myfunc = o()
    elif check == "p" or check == "P":
        myfunc = p()
    elif check == "q" or check == "Q":
        myfunc = q()
    elif check == "r" or check == "R":
        myfunc = r()
    elif check == "s" or check == "S":
        myfunc = s()
    elif check == "t" or check == "T":
        myfunc = t()
    elif check == "u" or check == "U":
        myfunc = u()
    elif check == "v" or check == "V":
        myfunc = v()
    elif check == "w" or check == "W":
        myfunc = w()
    elif check == "x" or check == "X":
        myfunc = x()
    elif check == "y" or check == "Y":
        myfunc = y()
    elif check == "z" or check == "Z":
        myfunc = z()

#final for loop for printing star formation word of user input
for i in range(length):
    i += 1
    check = (f"{L1[i-1]}")
# print(check)
    comput = func_iter()
    print("\n")
