def dup(nums):
    l=1
    for r in range(1,len(nums)):
        if nums[r]!=nums[r-1]:
            nums[l] = nums[r]
            l += 1
    return l

a=[0,0,1,2,3,3,4,4,4,5,5,5,]
d=dup(a)
print(d)
