def _xor(a):
    return bytes([x ^ 13 for x in a])
    

string = b'label'
new_string = _xor(string).decode()
flag = 'crypto{' + new_string + '}'
print(flag)
