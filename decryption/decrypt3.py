import hashlib

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
