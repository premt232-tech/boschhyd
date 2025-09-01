
dic_1 = {'a' :10 ,'b':20 ,'c':30}
dic_2= {'d':50,'a':10,'e':90}
merge_dic = dic_1.copy() 
for k,v in dic_2.items():
    merge_dic[k] = merge_dic.get(k,0)+v

print(f"the  result {merge_dic}")
