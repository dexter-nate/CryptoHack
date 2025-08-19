from vectors import scalar_prod
from math import sqrt


# Vector
v = [4,6,2,5]


'''
sage: res = v.norm()
'''
def vector_size(v):
    return sqrt(scalar_prod(v, v))


if __name__ == '__main__':
    res = vector_size(v)
    print(f'{res=}')
