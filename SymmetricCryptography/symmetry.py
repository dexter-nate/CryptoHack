import requests as r
from pwn import xor

base_url = 'https://aes.cryptohack.org/symmetry/'
s = r.Session()

iv_ct = s.get(base_url + 'encrypt_flag').json()['ciphertext']
iv = iv_ct[:32]
print(f'{iv=}')
ct = iv_ct[32:]
print(f'{ct=}', len(ct))
pt = (b'A' * 48).hex()

enc = s.get(base_url + 'encrypt/' + pt + '/' + iv).json()['ciphertext']
c1 = enc[:32]
c2 = enc[32:64]
c3 = enc[64:]

iv_enc1 = xor(bytes.fromhex(c1), b'A' * 16)
iv_enc2 = xor(bytes.fromhex(c2), b'A' * 16)
iv_enc3 = xor(bytes.fromhex(c3), b'A' * 16)

flag1 = xor(iv_enc1, bytes.fromhex(ct[:32]))
flag2 = xor(iv_enc2, bytes.fromhex(ct[32:64]))
flag3 = xor(iv_enc3, bytes.fromhex(ct[64:]))
flag = (flag1 + flag2 + flag3)[:33]
print(flag)
