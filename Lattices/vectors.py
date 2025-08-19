# Vectors 
v= [2,6,3]
w= [1,0,0]
u= [7,7,2]


'''
sage: s*v
'''
def scalar_mult(s, v):
    new_v = [0]*len(v)  # lista nuova
    for i in range(len(v)):
        new_v[i] = s * v[i]
    return new_v


'''
sage: v1+v2
'''
def vector_sum(v1, v2, sign='-'):
    if sign == '+':
        return [a + b for a, b in zip(v1, v2)]
    else:
        return [a - b for a, b in zip(v1, v2)]


'''
sage: v1.dot_product(v2)  # inner product
'''
def scalar_prod(v1, v2):
    res = 0
    for a, b in zip(v1, v2):
        res += a*b
    return res


'''
sage: v1.cross_product(v2)
'''
if __name__ == '__main__':
    r1 = scalar_mult(2, v)
    r2 = vector_sum(r1, w)
    r3 = scalar_mult(3, r2)
    r4 = scalar_mult(2, u)
    
    # res = 3⋅(2⋅v-w)⋅2⋅u
    res = scalar_prod(r3, r4)
    print(f'{res=}')
