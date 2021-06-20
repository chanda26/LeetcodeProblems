# [1,2,2,3,1]
from collections import Counter
def findshortestsubarray(lst):
    x=Counter(lst)
    max_ele={}
    unq=set(lst)
    for i in unq:
        max_ele[i]=x[i]
    m=max(sorted(max_ele.values()))
    ele=[ i for i,k in max_ele.items() if k==m]
    values=[]
    for k in ele:
        poslist = []
        for i,j in enumerate(lst):
                if j==k:
                    poslist.append(i)
        y=(poslist[-1]-poslist[0])+1
        values.append(y)
    return min(values)

print(findshortestsubarray([1,2,2,3,1,4,2]))