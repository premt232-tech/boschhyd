





a= list(map(int,input().split()))
b = list(map(int,input().split()))
c = [ item for item in a if item in b]
print(f"common elements {c}")