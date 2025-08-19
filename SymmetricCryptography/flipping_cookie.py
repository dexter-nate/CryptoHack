import requests as r
from pwn import xor

base_url = 'https://aes.cryptohack.org/flipping_cookie/'
s = r.Session()

cookie = s.get(base_url + 'get_cookie').json()['cookie']
print(f'{cookie=}')

iv = bytes.fromhex(cookie[:32])
ct = cookie[32:]
c1 = bytes.fromhex(ct[:32])
p1 = b'admin=False;expi'

partial_dec = xor(p1, iv)
print(f'{partial_dec=}')

new_p1 = b'admin=True;expir'
new_iv = xor(new_p1, partial_dec)

flag = s.get(base_url + 'check_admin/' + ct + '/' + new_iv.hex()).json()['flag']
print(flag)
