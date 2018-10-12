# Theodore Johnson
# 11/17/15
# Solving Linear Diophantine Equations



a = int(input("Enter an Integer for A:"))
b = int(input("Enter an Integer for B:"))
d = int(input("Enter an Integer for D:"))

aa = a
bb = b
r = aa%bb

# Finding the GCD

while r != 0:
    aa = bb
    bb = r
    r = (aa%bb)

print ("The GCD is",bb)

#Checking if there's a solution

if (d%bb) != 0:
    print ("There is no solution.")
    exit
else:
    print (bb, "divides",d,"There is a solution")

#Solving the Diophantine Equation
    
counter = 0

for i in range (-1*abs(b),abs(b)):
    for j in range (-1*abs(a),abs(a)):
        if (a*i + b*j) == d:
            print ("x =",i,"+",b,"t")
            print ("y =",j,"-",a,"t")
            exit()
