a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))

# opertion selection
o = input("Select operation (+, -, *, /): ")
match o:
    case '+':
        print(a,"+",b,"=",a+b)
    case'-':
        print(a,"-",b,"=",a-b)
    case '*':
        print(a,"*",b,"=",a*b)
    case '/':
        if b!=0 :
            print(a,"/",b,"=",a/b)
        elif b==0:
            print("b can not zero if you want to divide")

