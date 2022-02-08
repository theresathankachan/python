n = input("Enter final year: ")
p=[year for year in range(2020,int(n)) if (year%400==0) or (year%100 and year%4==0)]
print(p)
