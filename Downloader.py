import urllib.request
import os

def download_with_progress(url, output_file):
    def report_progress(block_num, block_size, total_size):
        downloaded = block_num * block_size
        percentage = downloaded / total_size * 100 if total_size > 0 else 0
        print(f"\rDownloading: {percentage:.2f}% ({downloaded / 1024:.2f} KB of {total_size / 1024:.2f} KB)", end="")

    try:
        print(f"Downloading file from {url}")
        urllib.request.urlretrieve(url, output_file, reporthook=report_progress)
        print(f"\nDownload completed: {output_file}")
    except Exception as e:
        print(f"Error during download: {e}")

# Main program
if __name__ == "__main__":
    # URL of the file to download
    file_url = "https://download.nikonimglib.com/archive2/payY500AHbkQ02bXMhb14TZo4978/D3300_NT(En)02.pdf"
    
    # Output file path - file type must match with download link file type (PDF -> PDF)
    save_path = os.path.join(os.getcwd(), "nikonimglib.pdf")

    # Start the download
    download_with_progress(file_url, save_path)