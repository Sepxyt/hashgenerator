import hashlib
import os

def hashed_text(text):
    encoded = text.encode()
    md5 = hashlib.md5(encoded).hexdigest()
    sha256 = hashlib.sha256(encoded).hexdigest()
    return md5, sha256

def hashed_file(filepath):
    if not os.path.exists(filepath):
        return None, None

    md5_hash_file = hashlib.md5()
    sha256_hash_file = hashlib.sha256()

    with open(filepath, 'rb') as f:
        while chunk := f.read(4096):
            md5_hash_file.update(chunk)
            sha256_hash_file.update(chunk)

    return md5_hash_file.hexdigest(), sha256_hash_file.hexdigest()

def main():
    print("Hash Generator (MD5 & SHA256")
    print("1 for TEXT")
    print("2 for FILE")
    choice = input("Enter 1 for Text or 2 for File: ").strip()

    if choice == "1":
        user_input = input("Enter Text to Hash: ")
        md5, sha256 = hashed_text(user_input)
        print(" ")
        print("Hashes:")
        print("MD5:    ", md5)
        print("SHA256:   ", sha256)
    elif choice == "2":
        filepath = input("Enter file path: ").strip()
        md5, sha256 = hashed_file(filepath)
        if md5 and sha256:
            print("Hashes for: ", filepath)
            print("MD5: ", md5)
            print("SHA256: ", sha256)
        else:
            print("File not found or couldnt be read ")

    else:
        print("Invalid choice, Enter 1 or 2")

if __name__ == "__main__":
    main()