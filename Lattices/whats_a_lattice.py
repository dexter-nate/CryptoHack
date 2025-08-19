# Vectors 
v1 = [6, 2,-3]
v2 = [5, 1, 4]
v3 = [2, 7, 1]

B = [v1, v2, v3]


'''
sage: res = B.det()
'''
def sarrus_det(B):
    x1 = B[0][0] * B[1][1] * B[2][2]
    x2 = B[1][0] * B[2][1] * B[0][2]
    x3 = B[2][0] * B[0][1] * B[1][2]
    
    y1 = B[0][2] * B[1][1] * B[2][0]
    y2 = B[1][0] * B[0][1] * B[2][2]
    y3 = B[0][0] * B[1][2] * B[2][1]
    
    res = (x1 + x2 + x3) - (y1 + y2 + y3)
    return abs(res)


if __name__ == '__main__':
    res = sarrus_det(B)
    print(f'{res=}')
