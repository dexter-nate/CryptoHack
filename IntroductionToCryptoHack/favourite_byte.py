from pwn import xor


enc = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

first_byte = enc[0]
for b in range(0, 256):
    tmp_k = bytes.fromhex(hex(b)[2:].zfill(2))
    if xor(first_byte, tmp_k) == b'c':
        key = tmp_k * len(enc)
        print(f'found byte: {tmp_k} --> key: {key}')
        break

flag = xor(key, enc).decode()
print(flag)
   