a=open ("file1.txt", "r")
b=[]
c=a.read()
b=c.split("\n")
x=b
a.close()
d=open ("file2.txt", "r")
e=[]
f=d.read()
e=f.split("\n")
y=e
d.close()
j=[]
j=b
b=e
e=j
aa= open ("file1.txt", "a")
for i in range (0,len(e)):
    aa.write (str( e[i]))
    i=i+1
aa.close()


    
