a = input("Enter a string ends with ing:")
if a.endswith("ing"):
    a += "ly"
else:
    a += "ing"
print("Replaced string:",a)    
