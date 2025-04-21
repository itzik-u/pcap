from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# 🔑 מפתח הצפנה (חייב להיות באורך 16, 24 או 32 בתים)
key = b'ThisIsA16ByteKey'

# 📄 הטקסט שברצוננו להצפין
plaintext = b'Secret message for CBC mode'

# 🧊 יצירת IV (וקטור אתחול) באורך 16 בתים
iv = get_random_bytes(16)

# 🛡️ הצפנה
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

print("Ciphertext (hex):", ciphertext.hex())

# 🔓 פענוח
decipher = AES.new(key, AES.MODE_CBC, iv)  # חשוב להשתמש באותו IV!
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("Decrypted:", decrypted.decode())
