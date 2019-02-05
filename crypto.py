import filecmp
import random,json

keys = []
encoder = {}
decoder = {}

def make_keys(s=100):
    keys = []
    while len(set(keys)) < s:
        keys.append( str(int(s*random.random())))
    return set(keys)

def save( a, b):
    f = open(a,'w')
    f.write(b)
    f.close()

def load( a):
    return  open(a).read()

def encrypt(s):
    ret = []
    for x in s:
        i = x.decode('utf-8')
        if i in encoder.keys():
            ret.append( encoder[i])
        else:
            v = keys.pop()
            encoder[i] = v
            decoder[v] = i
            ret.append(v)
    save('encode.txt', json.dumps(encoder))
    save('decode.txt', json.dumps(decoder))

    ciphertext = ' '.join(ret)
    save('ciphertext.txt',  ciphertext)
    return ciphertext


def decode_and_write():
    ct = load( 'ciphertext.txt')
    decoder = json.load(open('decode.txt'))
    ret = []
    for i in ct.split(' '):
        ret.append( decoder[i])
    save('decoded_ciphertext.txt', ''.join(ret))

def compare_two():
    print filecmp.cmp( 'plaintext.txt', 'decoded_ciphertext.txt')

compare_two()