import os
os.environ['TERM'] = 'xterm'

from sage.all import * # type: ignore
from pwn import remote
import json

n = 512
p = 257
q = 6007
delta = int(round(q/p))

conn = remote('socket.cryptohack.org', 13412)
conn.recvuntil(b'flag?\n')

As = []
bs = []

for i in range(n):
    print(f'It n° {i}')
    data = json.dumps({"option": "encrypt", "message": "0"})
    conn.sendline(data.encode())
    enc = json.loads(conn.recvline(False))
    A = eval(enc['A'])
    b = int(enc['b'])  # b = A*S + m*delta + e --m=0--> b = A*S + e
    As.append(A)
    bs.append(b)

# High Precision Real Field (Least-Squares)
R = RealField(100) # type: ignore
M = Matrix(R, As) # type: ignore
v = vector(R, bs) # type: ignore

# To recover S: |e| < delta/2 (|e|< 23/2) --> Very Low Probability which|e|>11.5 with Normal Distribution with mean=0 & std=3.8
S_real = M.solve_right(v)
S_rec = vector(ZZ, [int(round(x)) for x in S_real]) # type: ignore
print("S_rec:", S_rec)


flag = ''
len_flag = 46
for i in range(len_flag):
    data = json.dumps({"option": "get_flag", "index": str(i)})
    conn.sendline(data.encode())
    enc = json.loads(conn.recvline(False))
    A_flag = list(eval(enc['A']))   
    b_flag = int(enc['b'])

    A_flag = vector(ZZ, A_flag) # type: ignore
    tmp = A_flag * S_rec  

    m = int(round((b_flag - tmp) / delta)) % p
    e = b_flag - tmp - m * delta

    flag += chr(m)
    print(flag)
    '''print("b_flag:", b_flag)
    print("A·S:", tmp)
    print("c int:", m, "=> c chr:", chr(m))
    print("error (~noise):", e)'''
    
print(flag)
