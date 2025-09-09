import requests
import os
import hashlib
from urllib.parse import urlparse

def get_safe_filename(url, used_filenames):
    """
    Extracts a safe filename from the URL or generates one if missing.
    Ensures no filename conflicts.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    if not filename or "." not in filename:  
        filename = "downloaded_image.jpg"
    
    # Prevent duplicates by appending numbers
    base, ext = os.path.splitext(filename)
    counter = 1
    while filename in used_filenames:
        filename = f"{base}_{counter}{ext}"
        counter += 1
    
    used_filenames.add(filename)
    return filename


def is_duplicate(content, downloaded_hashes):
    """
    Uses SHA-256 hash to detect duplicate image content.
    """
    file_hash = hashlib.sha256(content).hexdigest()
    if file_hash in downloaded_hashes:
        return True
    downloaded_hashes.add(file_hash)
    return False


def fetch_image(url, used_filenames, downloaded_hashes):
    """
    Fetches and saves a single image with precautions.
    """
    try:
        # Send request with safety precautions
        headers = {"User-Agent": "Ubuntu-Image-Fetcher/1.0"}
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()

        # Check important headers
        content_type = response.headers.get("Content-Type", "")
        content_length = response.headers.get("Content-Length")

        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return

        if content_length and int(content_length) > 10 * 1024 * 1024:  # 10 MB limit
            print(f"✗ Skipped (file too large): {url}")
            return

        # Check duplicates
        if is_duplicate(response.content, downloaded_hashes):
            print(f"✗ Skipped (duplicate): {url}")
            return

        # Save image
        filename = get_safe_filename(url, used_filenames)
        filepath = os.path.join("Fetched_Images", filename)

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ Error: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs
    urls = input("Enter image URLs (separated by spaces): ").split()

    # Prepare directories and sets
    os.makedirs("Fetched_Images", exist_ok=True)
    used_filenames = set()
    downloaded_hashes = set()

    for url in urls:
        fetch_image(url, used_filenames, downloaded_hashes)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
