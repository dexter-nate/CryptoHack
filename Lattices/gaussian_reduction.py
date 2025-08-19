from vectors import *
from size_and_basis import *


# Vectors
v=[846835985,9834798552]
u=[87502093,123094980]


'''
Algorithm for Gaussian Lattice Reduction

Loop
   (a) If ||v2|| < ||v1|| swap v1,v2
   (b) Compute m=⌊v1⋅v2/v1⋅v1⌉
   (c) If m=0, return v1,v2
   (d) v2= v2-m⋅v1
Continue Loop

sage: M = [v1, v2]
sage: M.LLL()
'''
def gaussian_reduction(matrix_base):
   v1 = matrix_base[0]
   v2 = matrix_base[1]
   while True:
      if vector_size(v2) < vector_size(v1):
         v1, v2 = v2, v1
         
      m = round(scalar_prod(v1, v2) / scalar_prod(v1, v1))
      if m == 0:
         return v1, v2
      v2 = vector_sum(v2, scalar_mult(m, v1), '-')
      

v1, v2 = gaussian_reduction([v, u])
print(f'res: {scalar_prod(v1, v2)}')
