ft = open("newtext.txt")
content = ft.read()
words = content.split()
lar = max(words,key = len)

print(f"the longest word is {lar}")

