def bub_sort(lt):
    
    for i in range(0,len(lt)):
        swapped = False
        for j in range(0,len(lt)-i-1):
            if lt[j] >lt[j+1]:
                lt[j],lt[j+1] = lt[j+1],lt[j]
                swapped = True
        if not swapped:
                break
        


lt = list(map(int,input().split()))
bub_sort(lt)
print(f"sorted list {lt}")
