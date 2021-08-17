import operator
strl=input("enter the string:")
d1=dict()
for c in strl:
        d1[c]=d1.get(c,0)+1
print(d1)
dsc=dict(sorted(d1.items(),key=operator.itemgetter(1),reverse=True))
print("descending=",dsc)
