def isanagrams(s1,s2):
    if len(s1)!= len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1==s2
st1 = input("enter the string : ")
st2 = input("enter the string : ")
result = isanagrams(st1,st2)
if(result):
    print(f"the two string are anagrams")
else:
    print(f"the two string are not anagrams")