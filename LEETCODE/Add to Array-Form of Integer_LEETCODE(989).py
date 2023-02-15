def addToArrayForm(self, num: List[int], k: int) -> List[int]:
    r=''
    for i in num:
        r+=str(i)
    r=int(r)+k
    ans=[]
    while r:
        ans.append(r%10)
        r=r//10
    return ans[::-1]
        