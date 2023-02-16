def twoSum(n,target):
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if target-n[i]==n[j]:
                return [i,j]
    return None
a=[2,7,11,15]
target=22
c=twoSum(a,target)
print(c)