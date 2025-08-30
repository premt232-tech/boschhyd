import math
def isprime(n):
    if n <=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
        
    return True



start = int(input("enter the start range :"))
end =int(input("enter the end range :"))
prime =[]

for i in range(start,end):
    if isprime(i):
        prime.append(i)
print(f"the prime number from the range {start},{end}is {prime}")  