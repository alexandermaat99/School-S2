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
