def is_quadratic_residue(a, p):
    # Legendre Symbol 
    tmp = pow(a, (p-1)//2, p)
    if tmp == 1:
        print(f'a: {a} is a quadratic residue mod p')
        return pow(a, (p+1)//4, p)
    elif tmp == p - 1:  # In modulo p, -1 è rappresentato come p-1
        print(f'a: {a} is not a quadratic residue mod p')
    elif tmp == 0:
        print(f'a: {a} is congruent to 0 mod p')
    return None


with open('ModularArithmetic/legendre_symbol.txt', 'rb') as fr:
    file_content = fr.readlines()
    p = int(file_content[0].strip().split(b'p = ')[1])
    ints = eval(file_content[2].strip().split(b'ints = ')[1])
    for i in ints:
        x = is_quadratic_residue(i, p)
        if x != None:
            x1 = x % p
            x2 = (-x) % p
            assert pow(x1, 2, p) == i
            if x1 > x2:
                print(f'{x1 = }')
            else:
                print(f'{x2 = }')
            break
  