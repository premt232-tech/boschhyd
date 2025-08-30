import math
def sec_max(lt):

    max_val = - math.inf
    sec_val = -math.inf
    if  len(lt)< 2:
        return "there no second space to find second max"
    for i in lt:
        if i > max_val :
            sec_val = max_val
            max_val = i
        elif i > sec_val and i != max_val:
            sec_val = i
    return sec_val
   



lt =list(map(int,input().split()))
result = sec_max(lt)
print(f"second max element in list {result}")