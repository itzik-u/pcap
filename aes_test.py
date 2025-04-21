from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'ThisIsA16ByteKey'  # חייב להיות באורך 16, 24 או 32 בתים
plaintext = b'Hello, AES ECB Mode!'  # חייב להיות כפול של 16 בתים אחרי padding

# הצפנה
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

print("Ciphertext (hex):", ciphertext.hex())

# פענוח
decipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("Decrypted:", decrypted.decode())
