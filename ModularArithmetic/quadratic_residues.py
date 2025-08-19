p = 29
ints = [14,6,11]


def find_quad_res(x, p):
    for a in range(1, p):
        tmp_qr = a**2 % p
        if tmp_qr == x:
             print(f'x: {x} is a quadratic residue: {a}**2 = {x} (mod {p})')
             return a
    return None


for i in ints:
    a = find_quad_res(i, p)
    if a != None:
        assert pow(-a, 2, p) == i
        print(f'found a: {a}')
