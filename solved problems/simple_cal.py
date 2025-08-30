

n1 = int(input("enter the number : "))
n2 = int(input("enter the number : "))
op = input("enter the operator to peform : ")
result = 0
if op =='+':
    result = n1+n2
elif op =='-':
    result = n1-n2
elif op == '*':
    result = n1*n2
elif op =='/':
    result = n1/n2
print(f"{n1}{op}{n2}is {result}")
