from requests_html import HTMLSession
import os

WEBSITE_URL = 'https://www.classcentral.com/'

ENGLISH_DIR = 'EN'
SUBPAGES = 'subpages'
ENGLISH_SUBDIR = os.path.join(ENGLISH_DIR, SUBPAGES)
EN_INDEX_DIR = os.path.join(ENGLISH_DIR, 'index.html')
EN_INDEX_DIR_PRE = os.path.join(ENGLISH_DIR, 'index_pre.html')
JS_DIR = os.path.join('js/')

HINDI_DIR = 'HI'
HINDI_SUBDIR = os.path.join(HINDI_DIR, SUBPAGES)
HINDI_INDEX_DIR = os.path.join(HINDI_DIR, 'index.html')

SESSION = HTMLSession()

HEADERS = {
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "Accept-Language": "hi;q=0.9",
    "Content-Language": "hi;q=0.9",
    "Cookie": "googtrans=/en/hi",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
}
