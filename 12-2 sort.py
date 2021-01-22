num=int(input())
members=[]
for i in range(num):
    members.append([])
for i in range(num):
    members[i]=[int(x) for x in input().split()]
members.sort(key=lambda s:(s[0][len(s[0])-1],s[0][1],int(s[0][0:len(s[0])-1])
for i in range(num):
    if i>0:
        print("")
    print(members[i][0]+" "+members[i][1],end="")
