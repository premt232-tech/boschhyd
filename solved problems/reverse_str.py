def rev_st(a):
    rev = ""
    for i in a:
        rev = i + rev
    return rev
a = input("enter the string to reverse : ").strip()
result = rev_st(a)
print(f"the reversed string {result}")
