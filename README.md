# Nowa Era Book Downloader

This script is designed to download books from Nowa Era's flipbook platform.

**Prerequisites:**

* Python 3 (https://www.python.org/downloads/)
* Libraries: `requests`, `os`, `img2pdf`

  You can install them using pip:
  
  `pip install requests img2pdf`

Installation:
 * Clone this repository using git:

   `git clone https://github.com/GrafKiedyOdcinek/NowaEraDownloader`

Usage:
 * Navigate to the downloaded directory in your terminal.
 * Run the script:
python3 NowaEraDownloader.py

How it Works:
 * The script prompts you for the book link.
 * It extracts the book content from the provided URL.
 * It downloads all book pages as images and saves them in a folder named after the book title.
 * It creates a PDF file containing all the downloaded images, also named after the book title.
Disclaimer:
This script is intended for educational purposes only. It's recommended to respect the website's terms of service and copyright restrictions.
Further Enhancements:
Feel free to modify the script to:
 * Implement multithreading for faster downloads.
 * Add custom headers to mimic browser behavior.
Original fliphtml5Downloader Script:
This script was originally designed for downloading books from the fliphtml5 platform. You can find the original script and its documentation here: https://github.com/EngrMoazDev/fliphtml5Downloader
