def rem_dup(a):
    new_lt =[]
    for i in a:
        if i not in new_lt:
            new_lt.append(i)
    return new_lt




a = list(map(int,input().split()))
print(f"before duplicate the list {a}")
result = rem_dup(a)
print(f"after duplicate the list {result}")