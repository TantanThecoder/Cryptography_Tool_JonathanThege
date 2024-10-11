from cryptography.fernet import Fernet
import argparse

parser = argparse.ArgumentParser(description="Decrypt an encrypted text")

parser.add_argument("File_name", help="Name of the file to decrypt")
parser.add_argument("Output_file_name", help="Name of the file the output is stored in", default="Decrypted_message.txt")
parser.add_argument("-k", "--key", help="Enter the name of the file containing the cryptography key", default="generated.key")
args = parser.parse_args()

with open(args.key, "rb") as key_file:
   cipher_key = key_file.read()

cipher_suite = Fernet(cipher_key)

with open(args.File_name, "rb") as encrypted_file:
    encrypterd_text = encrypted_file.read()

decrypted_text = cipher_suite.decrypt(encrypterd_text)

with open(args.Output_file_name, "wb") as decrypted_file:
    decrypted_file.write(decrypted_text)


#öppnar filnamnet på encryptade filen, tas in via args!
#content läggs i en variabel som vi sen decryptar in i en ny variabel
#printa eller lägg decryptat meddelande i en fil

