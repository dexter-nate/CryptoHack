from pwn import xor


k1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k2_xor_k1 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
k2_xor_k3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flag_xor_k1_xor_k2_xor_k3 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

k2 = xor(k1, k2_xor_k1)
print(f'{k2 = }')

k3 = xor(k2, k2_xor_k3)
print(f'{k3 = }')

flag = xor(flag_xor_k1_xor_k2_xor_k3, k1, k2, k3).decode()
print(flag)

