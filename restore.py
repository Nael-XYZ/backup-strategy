#!/usr/bin/env python3
"""Restore from encrypted backup."""
import subprocess
import sys

def restore(backup_file, host, port, dbname):
    if backup_file.endswith(".gpg"):
        subprocess.run(["gpg", "--decrypt", backup_file], check=True)
        backup_file = backup_file[:-4]
    
    cmd = f"gunzip -c {backup_file} | psql -h {host} -p {port} {dbname}"
    subprocess.run(cmd, shell=True, check=True)
    print(f"Restored {backup_file} to {host}:{port}/{dbname}")

if __name__ == "__main__":
    restore(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4])
