a = str(input("Please Input an Integer: "))

#Jahdel Proofing
while str(a) == '':
    a = input("Please Input Something: ")
while str(a) != '':
    try:
        a = int(a)
        if a <= 0:
            a = input("Please Input a Non-Zero, Non-Negative Integer: ")
        elif a == 1:
            a = input("Not 1, Choose Another: ")
        else:
            break
 
    except ValueError:
        a = input("Please Enter an Integer: ")
        while str(a) == '':
            a = input("Please Input Something: ")
else:
    a = input("Please Input Something: ")

print(a)
