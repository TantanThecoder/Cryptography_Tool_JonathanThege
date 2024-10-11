from cryptography.fernet import Fernet
import argparse

parser = argparse.ArgumentParser(description="Encrypt a message or text")

parser.add_argument("File_name", help="Name of the file you want to store the enctypted message in")
parser.add_argument("Message", help="The message to be encrypted!")
parser.add_argument("-k", "--key", help="Enter the name of the file containing the cryptography key", default="generated.key")

args = parser.parse_args()

with open(args.key, "rb") as key_file:
    cipher_key = key_file.read()
  

cipher_suite = Fernet(cipher_key)

meddelande = args.Message.encode()

cipher_text = cipher_suite.encrypt(meddelande)
if ".enc" in args.File_name:
    with open(args.File_name, "wb") as encrypt_file:
        encrypt_file.write(cipher_text)
else:
    edited_file_name = args.File_name + ".enc"
    with open(edited_file_name, "wb") as encrypt_file:
        encrypt_file.write(cipher_text)



#argument som ska tas! 
#Filnamn
#Ska nyckel plockas direkt från mappen eller ska den läggas in
#av användaren?
 