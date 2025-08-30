def rotate_pos(lt, k):
    k = k%len(lt)
    return lt[k:] +lt[:k]





lt = list(map(int,input().split()))
k = int(input("ente the pos"))
print(f"rotate list {rotate_pos(lt,k)}")
