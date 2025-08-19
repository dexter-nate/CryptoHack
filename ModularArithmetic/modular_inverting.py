# For all elements g in the field, there exists a unique integer d such that g⋅d ≡ 1 (mod p) [d := modular inverse of g]

g = 3
p = 13

d = pow(g, -1, p)
print(f'{d = }')