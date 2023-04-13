eqn1=input("Enter the symbolic eqn:")
eqn=""
if(eqn1[0]!='-'):
    eqn="+"+eqn1
else:
    eqn=eqn1
l=[]
l1=[]
l2=[]
for i in range(len(eqn)):
    if(eqn[i]=='+'):
        l.append(i)
    elif(eqn[i]=='-'):
        l.append(i)
l.append(len(eqn)) 

for i in range(len(l)-1):
    l1.append(eqn[l[i]:l[i+1]])

for i in l1:
    if (i[0]=='+') and (i[1].isalpha()):
        l2.append("+1"+i[1:])
    elif(i[0]=='-' and (i[1].isalpha())):
        l2.append("-1"+i[1:])
    else:
        l2.append(i)

d={}
for i in range(len(l2)):
    s=0
    for j in range(len(l2)):
            if(l2[i][2:]==l2[j][2:] and i!=j):
                s+=int(l2[i][:2])+int(l2[j][:2])
    if s!=0:
        d[l2[i][2:]]=s

ans=""


for i in l2:
    if i[2:] not in list(d.keys()):
        d[i[2:]]=1

for i,j in d.items():
    
    if(j==0):
        continue
    else:
        ans+=str(j)+str(i)+'+'
        
ans=ans[:len(ans)-1]

ans1=''
for i in range(len(ans)):
    if(ans[i]=='+' and ans[i+1]=='-'):
        ans1+=''
    else:
        ans1+=ans[i]

print("answer is ",ans1)
