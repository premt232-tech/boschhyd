''' A left rotation operation on an array of size n shifts each of the array's elements 1 unit to 
the left. Given an integer, d, rotate the array that many steps left and return the result. '''

def rot(lt,k):
    k = k%len(lt)
    return lt[k:]+lt[:k]
lt = list(map(int, input("enter a data").split()))
k = int(input("enter number of rotation :"))
result = rot(lt,k)
print(result)