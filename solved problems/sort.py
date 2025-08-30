def sort_lt(lt):

    for i in range(0,len(lt)-1):
        for j in range(i+1,len(lt)):
            if lt[i]> lt[j]:
                lt[i] ,lt[j] = lt[j] ,lt[i]


lt = list(map(int,input().split()))
print(f"before sort {lt}")
sort_lt(lt)
print(f"after sort {lt}")