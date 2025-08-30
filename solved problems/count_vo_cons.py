def count_vc(s):
    vowels ="aeiou"
    num_v = 0
    num_c= 0
    for i in s:
        if i in vowels:
            num_v+=1
        elif i ==" ":
            pass
        else:
            num_c+=1
    return num_v,num_c

st = input("enter the sentance :").strip()
numb_vo ,numb_co = count_vc(st)
print(f"the number of vowels and consonants present in string {numb_vo} ,{numb_co}")