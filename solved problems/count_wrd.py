
fl = open("newtext.txt")
content = fl.read()
words = content.split()
count_words = len(words)
print(f"number of word in txt file is {count_words}")