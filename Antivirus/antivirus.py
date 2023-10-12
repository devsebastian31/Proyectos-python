import os
import hashlib

def scan_file(path):
    with open(path, 'rb') as f:
        content = f.read()
    hash = hashlib.sha256(content).hexdigest()
    if hash in malicious_hashes:
        print(f"WARNING: {path} is infected!")
    else:
        print(f"{path} is clean.")

def scan_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            scan_file(file_path)

# List of known malicious hashes
malicious_hashes = ['a5b69f8e2f9cfaa239deca4ad927f8e4f4d38e4dc153d69f2902af438f61bca7', '...']

# Scan the current directory
scan_dir('D:\Programacion\Python\Antivirus\Prueba')