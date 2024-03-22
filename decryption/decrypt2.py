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
