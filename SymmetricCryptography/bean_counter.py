import requests as r
from pwn import xor


base_url = 'https://aes.cryptohack.org/bean_counter/encrypt/'
s = r.Session()

ct = s.get(base_url).json()['encrypted']

ct_blocks = [ct[i:i+32] for i in range(0, len(ct), 32)]
header_png = bytes.fromhex('89504E470D0A1A0A0000000D49484452')
assert len(header_png) == 16

partial_enc_ctr = xor(header_png, bytes.fromhex(ct_blocks[0]))
png_bytes = b''
for b in ct_blocks:
    png_bytes += xor(partial_enc_ctr, bytes.fromhex(b))


with open("SymmetricCryptography/bean_flag.png", 'wb') as f:
    f.write(png_bytes)
