# Online Python - IDE, Editor, Compiler, Interpreter

n=int(input("Enter n value" ))
i=1
while i<=n:
    print(i,end="")
    i=i+1




#for loop
for i in range(5):
    for j in range(5):
        print("*",end="")
    print("")


for i in range(10):
    if i==7:
        break
    else:
        print(i)

#while loop
i=1
while i<=10:
    if i==5:
        pass
    print(i)
    i=i+1




#mathematics

#1


import math

print (math.ceil(10.2))


#2

import math

n = 2.5

print(str(math.ceil(n)))

#functions
def display(str):
    print("hello", str , "welcome to python")
display("python")



