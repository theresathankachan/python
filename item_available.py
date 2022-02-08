#evenodd
n=int(input("enter a number:"))
s=n%2
print("even") if s==0 else print("odd") 
#---------------------------------------
#item
l=['1','2','3']
item=input("enter an item:")
print("Available") if item in l else print("not available")
#-----------------------------------------------------------
#str list
l=["lilly","rose","lotus"]
item=input("enter a flower name:")
print("Available") if item in l else print("not available")


