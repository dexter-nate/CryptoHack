from pwn import xor


enc = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
crib = b'crypto{'
tmp = enc[:len(crib)]

key = xor(crib, tmp) + b'y'
print(f'{key = }')

len_key = len(enc) // len(key)
key *= len_key

flag = xor(key, enc).decode()
print(flag)
