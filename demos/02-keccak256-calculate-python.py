# First install "pycryptodome" (https://www.pycryptodome.org)
#   pip install pycryptodome

from Crypto.Hash import keccak
import binascii

text = 'hello'
data = text.encode("utf8")

keccak256 = keccak.new(data=data, digest_bits=256).digest()
print("Keccak256: ", binascii.hexlify(keccak256))
