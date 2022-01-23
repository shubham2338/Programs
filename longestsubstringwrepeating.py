'''
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3'''

def slicings(s):
    if len(s)==0:return 0
    max_length,start=0,0
    maps={}
    for i in range(len(s)):
        if (s[i] in maps and start<=maps[s[i]]):
            start = maps[s[i]]+1
        else:
            max_length=max(max_length,i-start+1)
        maps[s[i]]=i
    return max_length

s="abcabcbb"
print(slicings(s))