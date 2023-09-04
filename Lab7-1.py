x=open ("num1.txt", "r")
w=[]
y=x.read()
z=y.split(",")
w=z
x.close()
a=open ("num2.txt", "r")
b=[]
c=a.read()
d=c.split(",")
a.close()
b=d
if len(w) == len (b) and b==w:
    print ("They are the same")
else:
    print ("They are not the same")

