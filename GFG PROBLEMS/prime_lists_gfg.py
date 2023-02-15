"""
Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""
import math
class Solution:
    def primeList(self, head : Optional['Node']) -> Optional['Node']:
        # code here
        def is_prime(x):
            if x<2:
                return False
            if x==2 or x==3:
                return True
            if x%2==0 or x%3==0:
                return False
            for i in range(5,int(math.sqrt(x))+1,6):
                if (x%i==0) or (x%(i+2)==0):
                    return False
            return True
        d=head
        while d is not None:
            h=d.data
            if not(is_prime(h)):
                f=h+1
                h=h-1
                c1,c=0,0
                while not(is_prime(f)):
                    f+=1
                    c1+=1
                while not(is_prime(h)) and h>=0:
                    h-=1
                    c+=1
                if c<c1:
                    ans=h
                elif c>c1:
                    ans=f
                else:
                    ans=min(h,f)
                d.data=ans
            d=d.next
        return head