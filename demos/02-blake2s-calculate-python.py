import hashlib, binascii

text = 'hello'
data = text.encode("utf8")

blake2s = hashlib.new('blake2s', data).digest()
print("BLAKE2s:   ", binascii.hexlify(blake2s))
