N=int(input())

first=1
diff=6
house_num=1

while N>first:
    house_num+=1
    first+=diff
    diff+=6

print(house_num)
