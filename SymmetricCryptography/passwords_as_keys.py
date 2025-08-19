import requests as r
from hashlib import md5
from Crypto.Cipher import AES


base_url = 'https://aes.cryptohack.org/passwords_as_keys'
s = r.Session()

# key = md5(pwd)
# enc = AES_ECB(key, pwd)
enc_flag = s.get(base_url + '/encrypt_flag').json()['ciphertext']
print(enc_flag)

with open('/home/nate27/University/CyberChallenge/WordList/wordlist2.txt') as f:
    words = [w.strip() for w in f.readlines()]

ciphertext = bytes.fromhex(enc_flag)

for w in words:
    password_hash = md5(w.encode()).hexdigest()    
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
        if b'crypto' in decrypted:
            print(f'{password_hash=}, {decrypted=}')
            break
    except ValueError as e:
        print(e)
        pass