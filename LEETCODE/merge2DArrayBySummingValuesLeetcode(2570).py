class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans=[]
        d1={}
        for i in nums1:
            if i[0] not in d1:
                d1[i[0]]=i[1]
        d2={}
        for i in nums2:
            if i[0] not in d2:
                d2[i[0]]=i[1]
            
        for k,v in d1.items():
            if k in d2:
                ans.append([k,v+d2[k]])
                d2.pop(k)
            else:
                ans.append([k,v])
     
        for k,v in d2.items():
            ans.append([k,v])
        ans.sort()
        return ans
            
        
        