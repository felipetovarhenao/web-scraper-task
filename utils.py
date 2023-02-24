from config import WEBSITE_URL, SESSION, HEADERS
from requests_html import HTMLResponse
from bs4 import BeautifulSoup
import translators as ts
import os


def get_url(path: str, url: str, force: bool = False) -> HTMLResponse:
    """ Retrieves html from a given url """
    if not force and os.path.exists(path):
        return
    try:
        response = SESSION.get(url, headers=HEADERS)
    except Exception as e:
        print(f'Error while retrieving {url}: {e}')
        return
    code = response.status_code
    if code != 200:
        print(f"failed GET request ({code}): {url}")
        return
    return response


def parse_href(url: str) -> str:
    """ Completes url if href is a relative path """
    return (WEBSITE_URL[:-1] if url[0] == '/' else "") + url


def translate_html(input: str, output: str, backend: str = 'google', force: bool = False):
    """ Translates html file """
    if not force and os.path.exists(output):
        return
    with open(input, 'rb') as f:
        soup = BeautifulSoup(f.read(), 'lxml')

    i = 0

    for elem in soup.body.find_all(recursive=True):
        if elem.string:
            trans = ts.translate_text(elem.string.text,
                                      translator=backend,
                                      from_language='en',
                                      to_language='hi',
                                      if_ignore_empty_query=True,
                                      if_ignore_limit_of_length=True)
            elem.string.replace_with(trans)
            i += 1
            print(f"{i}: {trans}")

    with open(output, 'w') as f:
        f.write(str(soup))
