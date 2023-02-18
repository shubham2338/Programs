class Solution:
    def appleSequences(self, n, f, arr):
        # code here
        mres=0
        j=0
        i=0
        m=f
        while j<n:
            if m>0:
                if arr[j]=='O':
                    m-=1
              
            else:
                if arr[j]=='O':
                    while arr[i]!="O":
                        i+=1
                    i+=1
            mres=max(j-i+1,mres)
            j+=1
        return mres