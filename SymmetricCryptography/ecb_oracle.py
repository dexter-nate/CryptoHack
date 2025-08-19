import requests as r
from string import printable
from Crypto.Util.Padding import pad


base_url = 'https://aes.cryptohack.org/ecb_oracle/encrypt/'
s = r.Session()

# Recover len
for i in range(1, 16):
    pt = '00' * i
    # ct = AES_ECB(pt + flag + padding)
    ct = s.get(base_url + pt).json()['ciphertext']
    print(f'{i} --> {len(ct)}')

flag_len = 25
print(f'{flag_len=}')

# Recover Last Block
flag = ''
idx = 8
for i in range(16):
    pt = '00' * idx
    ct = s.get(base_url + pt).json()['ciphertext']
    target = ct[-32:]  # last_block_ct
    print(f'{target=}')
    
    for c in printable:
        padded = pad((c+flag).encode(), 16).hex()
        ct = s.get(base_url + padded).json()['ciphertext']
        first_block = ct[:32]
        
        if target == first_block:
            idx += 1
            print(f'It {i} - Found c: {c}')
            flag = c + flag
            print(f'{flag=}')
            break

# Recover First Block
flag= '6u1n5_h473_3cb}'
idx = 7
for i in range(10):
    pt = '00' * idx
    ct = s.get(base_url + pt).json()['ciphertext']
    target = ct[-64:-32]  # last_block_ct
    print(f'{target=}')

    for c in printable:
        padded = ((c+flag).encode()).hex()
        ct = s.get(base_url + padded).json()['ciphertext']
        first_block = ct[:32]
        
        if target == first_block:
            idx += 1
            print(f'It {i} - Found c: {c}')
            flag = c + flag
            print(f'{flag=}')
            break
