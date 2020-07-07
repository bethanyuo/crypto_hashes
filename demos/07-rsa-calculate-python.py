from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(2048)
pubKey = keyPair.publickey()
print(f"Public key: (mod={pubKey.n}, exp={pubKey.e})")
print("Private key:", keyPair.d)

encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(b'Some message')
print("Encrypted:", binascii.hexlify(encrypted))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)
