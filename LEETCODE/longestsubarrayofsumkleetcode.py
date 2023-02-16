#we have to longest sub array from a array
#a=[4,1,1,1,2,3,5] k=5 length of array is 7
def longestsub(a,t):
    sum=0
    i,j=0,0
    while(j<=len(a)):
        while sum<t:
            sum=sum+a[j]
            j+=1
        if sum==t:
            sum=max(sum,i-j+1)
            j+=1
        while t<sum:
             sum = sum-a[i]
             i+=1
        j+=1
    
    return sum
a=[4,1,1,1,2,3,5]
t=5
print(longestsub(a,t))
