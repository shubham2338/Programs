def dup(nums,t):
    l=0
    for r in range(len(nums)):
        if nums[r]!=t:
            nums[l] = nums[r]
            l += 1
    return l

a=[3,2,2,3]
t=2
d=dup(a,t)
print(d)

