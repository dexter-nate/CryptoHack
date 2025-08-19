from sympy.ntheory.modular import crt

n = [5, 11, 17]
c = [2, 3, 5]

x = crt(n, c)
print(f'x: {x[0]}')
