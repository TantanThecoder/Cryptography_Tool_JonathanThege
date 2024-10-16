from cryptography.fernet import Fernet
import argparse

parse = argparse.ArgumentParser(description="Key generator, do not change the name of the file key is stored in!")
parse.add_argument("-f", "--file_name", help="Enter the name of the file to store the key in! If not entered a defult name will be given!", default="generated.key")
key = Fernet.generate_key()

args = parse.parse_args()

with open(args.file_name, "wb") as key_file:
    key_file.write(key)

print("A key has been saved!")




