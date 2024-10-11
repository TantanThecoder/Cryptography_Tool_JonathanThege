from cryptography.fernet import Fernet
import argparse

parse = argparse.ArgumentParser(description="Key generator, do not change the name of the file key is stored in!")

key = Fernet.generate_key()

with open("generated.key", "wb") as key_file:
    key_file.write(key)

print("A key has been saved!")




