def pali(s):
    return s == s[::-1]



st = input("enter the string : ")
if(pali(st.strip())):
    print("the  strings is palindrome")
else:
    print("the  strings is not  palindrome")
