line=input("enter a string:")
count=[word for word in line.split() if word.isalpha()]
print(len(count))
