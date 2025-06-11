import os
import sys

def find_files_with_magic(root_path, magic_bytes):
    magic_len = len(magic_bytes)
    found_files = []

    print(f"Scanning folder: {root_path}")
    print(f"Looking for magic bytes: {magic_bytes.hex().upper()} at file start\n")

    for foldername, _, filenames in os.walk(root_path):
        for filename in filenames:
            full_path = os.path.join(foldername, filename)
            try:
                with open(full_path, 'rb') as f:
                    header = f.read(magic_len)
                    if header == magic_bytes:
                        print(f"[MATCH] {full_path}")
                        found_files.append(full_path)
                    else:
                        print(f"[NO MATCH] {full_path}")
            except Exception as e:
                print(f"[ERROR] Could not read {full_path}: {e}")

    print("\nScan complete.")
    if found_files:
        print(f"Found {len(found_files)} file(s) with the magic bytes:")
        for f in found_files:
            print(f"  - {f}")
    else:
        print("No files found with the specified magic bytes.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python SignatureTracking.py <folder_path>")
        sys.exit(1)

    folder_to_scan = sys.argv[1]
    magic = bytes.fromhex("AF1BB1FA")

    find_files_with_magic(folder_to_scan, magic)
