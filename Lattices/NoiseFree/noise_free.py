from pwn import remote
import json

def send_json(conn, obj):
    data = json.dumps(obj) + "\n"
    conn.sendline(data.encode()) 

    
conn = remote('socket.cryptohack.org', 13411)
conn.recvuntil(b'?\n')

json_data_1 = {"option":"get_flag", "index":""}
encs1 = []
for i in range(32):
    json_data_1['index'] = str(i)
    send_json(conn, json_data_1)
    
    enc = json.loads(conn.recv().decode())
    encs1.append(enc)

with open('Lattices/NoiseFree/encs1.txt', 'w') as f:
    f.write(str(encs1))
print("[+] Step 1 Completed")

json_data_2 = {"option": "encrypt", "message": ""}
encs2 = []
for _ in range(64):  # len secret
    json_data_2['message'] = str(0)
    send_json(conn, json_data_2)
    
    enc = json.loads(conn.recv().decode())
    encs2.append(enc)

with open('Lattices/NoiseFree/encs2.txt', 'w') as f:
    f.write(str(encs2))
print("[+] Step 2 Completed")
