def fac(num):
    if num == 0 or num == 1 :
        return 1
    return fac(num-1)*num

num = int(input("enter the number : "))
result = fac(num)
print(f"the factorial of {num} is {result}")