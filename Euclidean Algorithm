#Euclidean Algorithm Program

print("( a , b )")
alpha = int(input("Enter An Integer:"))
print("(",alpha,", b )")
beta = int(input("Enter A Second Integer:"))
print("(",alpha,",",beta,")")

if alpha > beta:
    a = alpha
    b = beta
else:
    a = beta
    b = alpha

r = a%b
s = a//b

print(a,"=",s,"*",b,"+",r)

while r != 0:
    a = b
    b = r
    r = a%b
    s = a//b
    print(a,"=",s,"*",b,"+",r)

print("The greatest common divisor is",b,)
