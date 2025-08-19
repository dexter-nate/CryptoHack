a = 288260533169915
p = 1007621497415251

with open('./ModularArithmetic/adriens_sign.txt', 'r') as f:
    ciphertext = list(f.read()[1:-2].split(', '))

# Test a == QR:
assert pow(a, (p-1)//2, p) == 1

'''
Criterio di Eulero (a è un residuo quadratico in Zp):
Se n = a^2 (mod p), allora n è un residuo quadratico in Zp.
Se n = -a^2 (mod p), allora n non è un residuo quadratico in Zp.
'''

plaintext_bits = []
for n in ciphertext:
    n = int(n)
    if pow(n, (p-1)//2, p) == 1:
        plaintext_bits.append('1')
    else:
        plaintext_bits.append('0')

plaintext = ''.join(plaintext_bits)

flag = ''.join(chr(int(plaintext[i:i+8], 2)) for i in range(0, len(plaintext), 8))
print(flag)