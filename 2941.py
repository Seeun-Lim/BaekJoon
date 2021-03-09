croatian=['c=','c-','d-','lj','nj','s=','z=']

N=input()

total=0
i=0

while True:
    if i<len(N)-3 and N[i]=='d' and N[i+1]=='z' and N[i+2]=='=':
        total+=1
        i+=3
    if i<len(N)-2:
        for j in croatian:



