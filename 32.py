import sys 
def cube(i):
    j=i*i*i
    return j
n= int(sys.argv[1])
for i in range(1,n+1):
    print('%s %s'%(5,cube(i)))
