import sys
import itertools

def _l(idx, s):
    return s[idx:] + s[:idx]

def decrypt(p,k1,k2):
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
    t = [[_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]
    i1 = 1
    i2 = 1
    c = ""
    for a in p:
        for num in range(len(s)):
            if t[num][s.find(k1[i1])][s.find(k2[i2])] == a:
                c+= s[num]
                i1 = (i1 + 1) % len(k1)
                i2 = (i2 + 1) % len(k2)
                break
    return c

def main(p, k1, k2):
# p is plaintext k1 is key k2 is gyaku key
    #s = "ABCDEFG"
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
    t = [[_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]
    i1 = 0
    i2 = 0
    c = ""
    for a in p:
        c += t[s.find(a)][s.find(k1[i1])][s.find(k2[i2])]
        i1 = (i1 + 1) % len(k1)
        i2 = (i2 + 1) % len(k2)
    return c

def key_crack(p,e,length):
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
    t = [[_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]
    i1 = 0
    i2 = 0
    tmp = 0
    plaintxt = ""
    ans = [0,0,0,0,0,0,0]
    key = "AAAAAAAAAAAAAA"
    key_list = list(key)
    for i in range(7):
        tmp = s.find(e[i]) + 65 - s.find(p[i])
        if tmp > 65 :
            ans[i] = tmp - 65
        else:
            ans[i] = tmp
    print ans
    for j in range(len(e)):
        plaintxt +=  s[(s.find(e[j]) + 65 - ans[j % 7]) % 65]
        
                                
    
    key = "".join(key_list)
    return plaintxt

def find_key(s,p1,e1):
    return 0
    
                     
#cipher = main("SECCON{", sys.argv[1], sys.argv[1][::-1])
plain = "SECCON{}"
encrypt = "POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9"
key = key_crack(plain,encrypt,14)
print key 
#plaintxt =  decrypt(encrypt,key,key[::-1])

#print key
#print decrypt("POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9",key,key[::-1])
