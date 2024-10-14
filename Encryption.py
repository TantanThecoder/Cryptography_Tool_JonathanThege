from cryptography.fernet import Fernet
import argparse

parser = argparse.ArgumentParser(description="Encrypt a message or text")

parser.add_argument("Data_type",choices=["File", "Terminal_input"] ,help="Choose either to encrypt a message from a file or an text input from the terminal!")
parser.add_argument("File_name", help="Name of the file you want to store the enctypted message in")
parser.add_argument("Message", help="Write filename or input the text to be encrypted depending on earlier choice!")
parser.add_argument("-k", "--key", help="Enter the name of the file containing the cryptography key", default="generated.key")

args = parser.parse_args()

try:
    with open(args.key, "rb") as key_file:
        cipher_key = key_file.read()
except FileNotFoundError:
    print(f"The file: {args.key} was not found!")
else:
    cipher_suite = Fernet(cipher_key)

if args.Data_type == "File":
    try:
        with open(args.Message, "rb") as text_file:
            message = text_file.read()
            cipher_text = cipher_suite.encrypt(message)
    except FileNotFoundError:
        print("Invalid file name!")
    else:
        print("File has been read!")
else:
    message = args.Message.encode()
    cipher_text = cipher_suite.encrypt(message)

if ".enc" in args.File_name:
    with open(args.File_name, "wb") as encrypt_file:
        encrypt_file.write(cipher_text)
else:
    edited_file_name = args.File_name + ".enc"
    with open(edited_file_name, "wb") as encrypt_file:
        encrypt_file.write(cipher_text)
