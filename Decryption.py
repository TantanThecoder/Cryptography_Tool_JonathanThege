from cryptography.fernet import Fernet
import argparse

parser = argparse.ArgumentParser(description="Decrypt an encrypted text")

parser.add_argument("File_name", help="Name of the file to decrypt")
parser.add_argument("Output_file_name", help="Name of the file the output is stored in", default="Decrypted_message.txt")
parser.add_argument("-k", "--key", help="Enter the name of the file containing the cryptography key", default="generated.key")
args = parser.parse_args()

try:
    with open(args.key, "rb") as key_file:
        cipher_key = key_file.read()
except FileNotFoundError:
    print(f"The file: {args.key} was not found!")
else:
    cipher_suite = Fernet(cipher_key)
    try:
        with open(args.File_name, "rb") as encrypted_file:
            encrypterd_text = encrypted_file.read()
    except FileNotFoundError:
        print(f"The file: {args.File_name} was not found!")
    else:
        decrypted_text = cipher_suite.decrypt(encrypterd_text)
        
        with open(args.Output_file_name, "wb") as decrypted_file:
            decrypted_file.write(decrypted_text)
