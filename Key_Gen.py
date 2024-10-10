from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("generated.key", "wb") as key_file:
    key_file.write(key)

print("A key has been saved!")




