words = {}
line=input("Enter a sentence:")
for w in line.lower().split():
    words[w] = words.get(w,0) + 1
print(words)
