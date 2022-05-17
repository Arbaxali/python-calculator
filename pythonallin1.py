def summ(a,op,b):
    if op == 'add':
        res=a+b
    elif op =='sub':
        res =a-b
    elif op =='mul':
        res = a*b
    elif op == 'div':
        res = a/b
    return res    
       
def OddorEven(a):

    if (a % 2)==0:
        res = "even"
    else:
        res =" odd"

    return res    
    
        
        


def calc(inp):
    if inp == 'cal':
        a = input("add num1 ")
        op= input("add operator ")
        b = input("add num2 ")
        a= int(a)
        b=int(b)
        res1 = summ(a,op,b)
        return res1 
    elif inp == 'ode':
        a = int(input("enter the number for checking odd or even"))
        res1 = OddorEven(a)
    return res1



res2 = input("what operation u would like to do? ")
res3 = calc(res2)

print(res3)


