import string
import argparse
from tqdm import tqdm

def is_valid_password(password):
    if not (4 <= len(password) <= 4):
        return False
    for char in password:
        if char not in string.ascii_letters + string.digits:
            return False
    return True

def filter_passwords(source_filename, target_filename):
    valid_passwords = 0
    total_passwords = sum(1 for _ in open(source_filename, 'r', errors="replace"))
    
    with open(source_filename, "r", errors="replace") as source_file, open(target_filename, "w") as target_file:
        for line in tqdm(source_file, total=total_passwords, desc="Filtering Passwords"):
            password = line.strip()
            if is_valid_password(password):
                valid_passwords += 1
                target_file.write(password + "\n")

    print(f"Found {valid_passwords} valid passwords.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter a password list based on specific criteria.")
    parser.add_argument("source_filename", help="The name of the source password list file.")
    parser.add_argument("target_filename", help="The name of the target file to write filtered passwords to.")

    args = parser.parse_args()

    filter_passwords(args.source_filename, args.target_filename)
