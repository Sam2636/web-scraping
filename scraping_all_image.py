import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """
    soup= bs(requests.get("https://rarible.com/").content, "html.parser")

    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue    

        img_url = urljoin(url, img_url)

    try:
        pos = img_url.index("?")
        img_url = img_url[:pos]
    except ValueError:
        pass

        if is_valid(img_url):
            urls.append(img_url)
    return urls


        