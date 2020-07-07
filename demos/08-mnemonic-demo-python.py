import mnemonic, binascii

words = 'tired galaxy demand fade bunker book treat oval near price bar extra'
entropy = mnemonic.Mnemonic('english').to_entropy(words)
print("Entropy (16 bytes):", binascii.hexlify(entropy))

seed = mnemonic.Mnemonic.to_seed(words)
print("Seed (64 bytes):", binascii.hexlify(seed))

wordsBack = mnemonic.Mnemonic('english').to_mnemonic(entropy)
print("Mnemonic (12 words):", wordsBack) 
