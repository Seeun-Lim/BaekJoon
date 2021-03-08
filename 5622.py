def dial(a):
    if a>='A' and a<='C':
        return 2
    elif a>='D' and a<='F':
        return 3
    elif a>='G' and a<='I':
        return 4
    elif a>='J' and a<='L':
        return 5
    elif a>='M' and a<='O':
        return 6
    elif a>='P' and a<='S':
        return 7
    elif a>='T' and a<='V':
        return 8
    elif a>='W' and a<='Z':
        return 9
    elif a=='OPERATOR':
        return 0
    else:
        return 1

word=input()
total=0
for i in range(len(word)):
    a=dial(word[i])
    total+=(a+1)
print(total)