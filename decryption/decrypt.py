from Crypto.Cipher import ChaCha20
from Crypto.Hash import SHA256

def decrypt_file(encrypted_path, decrypted_path, password, nonce):
    key = SHA256.new(password.encode()).digest()
    cipher = ChaCha20.new(key=key, nonce=nonce)

    with open(encrypted_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(decrypted_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print("Decryption Complete. Check the decrypted file.")

# Usage
password = "whodrinksroots"
nonce = b"abcdefgh"
decrypt_file('decryption\PO_encrypted.pdf', 'decryption/PO-decrypted.txt', password, nonce)

import hashlib

def hash_file_sha1(file_path):
    hasher = hashlib.sha1()
    with open(file_path, 'rb') as file:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: file.read(4096), b""):
            hasher.update(byte_block)
    return hasher.hexdigest()

# Hashing RootBeerTest365A.pdf
hash_a = hash_file_sha1('decryption\RootBeerTest365A.pdf')
print(f"SHA1 Hash of RootBeerTest365A.pdf: {hash_a}")

# Hashing RootBeerTest365B.pdf
hash_b = hash_file_sha1('decryption\RootBeerTest365B.pdf')
print(f"SHA1 Hash of RootBeerTest365B.pdf: {hash_b}")

# Comparing the hashes
if hash_a == hash_b:
    print("The files are identical.")
else:
    print("The files are different.")

def hash_file_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

md5_hash_file1 = hash_file_md5('decryption\console1.png')
md5_hash_file2 = hash_file_md5('decryption\console2.png')

print(md5_hash_file1, md5_hash_file2)

if md5_hash_file1 == md5_hash_file2:
    print("The files are the same.")
else:
    print("The files are different.")
