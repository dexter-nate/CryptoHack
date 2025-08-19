from egcd import egcd


#  a⋅u + b⋅v = gcd⁡(a,b) -->  p⋅u + q⋅v = gcd⁡(p,q) 
p=26513
q=32321

gcd_p_q, u, v = egcd(p, q)
print(gcd_p_q, u, v)