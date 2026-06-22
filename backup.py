#!/usr/bin/env python3
"""Automated encrypted backup script."""
import os
import subprocess
from datetime import datetime
from pathlib import Path

def backup_database(host, port, dbname, output_dir="/backups"):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/{dbname}_{timestamp}.sql.gz"
    
    cmd = f"pg_dump -h {host} -p {port} {dbname} | gzip > {filename}"
    subprocess.run(cmd, shell=True, check=True)
    
    encrypt_file(filename)
    upload_s3(filename)
    cleanup_old(output_dir, retention_days=30)
    return filename

def encrypt_file(filepath):
    key = os.environ.get("BACKUP_ENCRYPTION_KEY")
    if key:
        subprocess.run(["gpg", "--symmetric", "--cipher-algo", "AES256", filepath], check=True)
        os.remove(filepath)

def upload_s3(filepath):
    subprocess.run(["aws", "s3", "cp", filepath, "s3://backups-bucket/"], check=True)

def cleanup_old(directory, retention_days=30):
    subprocess.run(f"find {directory} -mtime +{retention_days} -delete", shell=True)
