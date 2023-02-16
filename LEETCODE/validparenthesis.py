def stack1(s):
    stack=[]
    for i in s:
        if i in "({[":
            stack.append(i)
        else:
            if i==")" and stack[-1]!="(":
                return False
            if i=="]" and stack[-1]!="[":
                return False
            if i=="}" and stack[-1]!="{":
                return False
            stack.pop()
    if len(stack)!=0:
        return False
    return True
s="{{}}"
p=stack1(s)
print(p)

            
