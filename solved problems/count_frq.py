
def cout_frq(a):
    cout_dic = {}
    for i in a:
        cout_dic[i] = cout_dic.get(i,0)+1
    return cout_dic




a = list(map(int,input().split()))


result = cout_frq(a)
print(f"the frequency of each number in list {result}")