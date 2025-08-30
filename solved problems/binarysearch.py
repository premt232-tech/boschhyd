def bin_s(lt ,t,low,high):
    if low>high:
        return -1
    mid = (low+high)//2
    if lt[mid] == t :
        return mid
    elif  t >lt[mid]:
        return bin_s(lt,t,mid+1,high)
    elif t < lt[mid]:
        return bin_s(lt,t,low,mid-1)




lt = list(map(int,input().split()))
target = int(input("enter the target"))
lt = sorted(lt)
result = bin_s(lt,target ,0 ,len(lt))
if(result):
    print(f"the element id found in index of{result}")
else:
    print("element not found")