from vectors import *
from size_and_basis import *


'''
Algorithm for Gram-Schmidt:

u1=v1
Loop i= 2,3,...,n
    u_ij = v_i * u_j / ||u_j||^2, (1 <= j < i)
    Set u_i = v_i - u_ij * u_j (Sum over j for 1 <= j < i)
End Loop 


sage: M = Matrix([v0, v1, v2, v3])
sage: M.gram_schmidt()
'''


# Vectors
v0 = [4, 1, 3,-1]
v1 = [2, 1,-3, 4]
v2 = [1, 0,-2, 7]
v3 = [6, 2, 9,-5]

B_matrix = []
B_matrix.append(v0)
B_matrix.append(v1)
B_matrix.append(v2)
B_matrix.append(v3)

n = 4
u0 = v0
B_star_matrix = [u0]
for i in range(1, n):
    v_i = B_matrix[i]
    u_i = v_i
    
    for j in range(0, i):
        u_j = B_star_matrix[j]
        dot = scalar_prod(v_i, u_j)
        mu_ij = dot / (vector_size(u_j) ** 2)
        
        proj = scalar_mult(mu_ij, u_j)
        u_i = vector_sum(u_i, proj, '-')
    
    B_star_matrix.append(u_i)

print(f'res={B_star_matrix[3][1]}')
