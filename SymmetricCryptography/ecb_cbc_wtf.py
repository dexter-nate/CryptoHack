import requests as r
from pwn import xor


base_url = 'https://aes.cryptohack.org/ecbcbcwtf/'
s = r.Session()

ciphertext = s.get(base_url + 'encrypt_flag').json()['ciphertext']
print(f'{ciphertext=}')

iv = ciphertext[:32]
ct = ciphertext[32:]
ct_blocks = [ct[i:i+32] for i in range(0, len(ct), 32)]

first_block_pd = s.get(base_url + 'decrypt/' + ct_blocks[0]).json()['plaintext']
print(f'{first_block_pd=}')

first_block_fd = xor(bytes.fromhex(iv), bytes.fromhex(first_block_pd))
print(first_block_fd)

second_block_pd = s.get(base_url + 'decrypt/' + ct_blocks[1]).json()['plaintext']
print(f'{second_block_pd=}')

second_block_fd = xor(bytes.fromhex(ct_blocks[0]), bytes.fromhex(second_block_pd))
print(second_block_fd)

flag = first_block_fd + second_block_fd
print(f'{flag=}')