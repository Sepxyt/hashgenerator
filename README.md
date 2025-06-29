#  Hash Generator (MD5 & SHA256)

A simple Python tool that generates **MD5** and **SHA256** hashes for any input text or file. Useful for verifying file integrity, password hashing, and learning how cryptographic hash functions work in cybersecurity.

---

##  Features

- Accepts **text** or **file input**
- Computes **MD5** and **SHA256** hashes
- Prints results in a clean, readable format
- Handles invalid paths and bad input gracefully
- 100% Python — no external libraries required

---

##  How It Works

Hashing is the process of converting any input (like a string or file) into a fixed-length string (called a *hash* or *digest*). Even a 1-character change results in a completely different hash.

This script uses Python's built-in `hashlib` module to compute two popular hashes:
- `MD5`: Fast, but no longer secure — used for checksums
- `SHA256`: Strong and secure — widely used in modern cybersecurity

---

##  Real-World Applications

1. ** File integrity checks** – verify downloads haven’t been tampered with  
2. ** Password hashing** – never store raw passwords, only store their hash  
3. ** Malware detection** – compare file hashes to known malware signatures  
4. ** Tampering detection** – detect unauthorized changes to config/system files  
5. ** Backup verification** – ensure large backups weren’t corrupted over time

---

##  How to Use

### 1. Clone the repo or download the script

```bash
git clone https://github.com/yourusername/hash-generator.git
cd hash-generator
python hash_generator.py


