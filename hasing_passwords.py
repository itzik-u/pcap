import hashlib

password = "123456"

# MD5
md5_hash = hashlib.md5(password.encode()).hexdigest()
print("MD5:", md5_hash)

# SHA-256
sha256_hash = hashlib.sha256(password.encode()).hexdigest()
print("SHA256:", sha256_hash)

passwords = ["123456","password","1234565"]

for password in passwords:
    if hashlib.md5(password.encode()).hexdigest() == md5_hash or hashlib.sha256(password.encode()).hexdigest() == sha256_hash:
        print(password)
