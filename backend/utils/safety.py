from pathlib import Path

ALLOWED_TEXT_EXTENSIONS = {".txt", ".eml"}
MAX_UPLOAD_BYTES = 1 * 1024 * 1024

def validate_safe_upload(filename: str, size: int):
    ext = Path(filename or "").suffix.lower()
    if ext not in ALLOWED_TEXT_EXTENSIONS:
        raise ValueError("Only .txt and .eml sample files are allowed.")
    if size > MAX_UPLOAD_BYTES:
        raise ValueError("Uploaded sample is larger than the 1 MB limit.")
