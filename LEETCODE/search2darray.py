# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
def mat(matrix,t):
    flag=False
    for i in matrix:
        if t in i:
            flag= True
    return flag

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
t=9
print(mat(matrix,t))