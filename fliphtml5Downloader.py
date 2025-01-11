import import requests
import os
import img2pdf

# Taking Book reference/link from user
book_link = input("Enter the book link: ")

# Ensure the link ends correctly (assuming the link points to the flipbook's main page)
url = book_link.rstrip("/")

# **Correctly encode the URL to handle special characters**
config_file_url = f"{url}/mobile/javascript/config.js"

try:
    # Request to get the config file
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    config_file = requests.get(config_file_url, headers=headers)
    config_file.raise_for_status()
    
    # Extract total pages from the config file
    try:
        total_pages = int(config_file.text.split('bookConfig.totalPageCount=')[1].split(';')[0])
    except IndexError:
        print("Couldn't find 'bookConfig.totalPageCount' in config file. Assuming single page.")
        total_pages = 1

    os.makedirs('bookdownload', exist_ok=True)

    # Let's download our images now
    page_images = []
    for page in range(total_pages):
        page_url = f'{url}/files/mobile/{page + 1}.jpg'
        file_path = f"bookdownload/{page + 1}.jpg"
        
        try:
            page_image = requests.get(page_url, headers=headers)
            page_image.raise_for_status()
            
            page_images.append(page_image.content)
            print(f'Downloading Page {page + 1} / {total_pages} .....')
            
            with open(file_path, "wb") as f:
                f.write(page_image.content)
        
        except requests.exceptions.RequestException as e:
            print(f"Failed to download page {page + 1}: {e}")
    
    if page_images:
        print("Downloading Complete. Don't close, hold on. We are yet to make the PDF.")

        # Let's make the PDF now.
        pdf_path = "bookdownload/bookdownload.pdf"
        with open(pdf_path, "wb") as file:
            file.write(img2pdf.convert(page_images))
        
        print(f'The PDF named {pdf_path} has been saved in your working directory.')
        print('Thank you for using this script.')
    
except requests.exceptions.RequestException as e:
    print(f"Failed to retrieve the config file: {e}")
