from bs4 import BeautifulSoup
from utils import get_url
from config import (
    EN_INDEX_DIR_PRE,
    WEBSITE_URL
)


def retrieve_index(path: str, url: str, force: bool = False) -> None:
    """ Retrieves html from a given url """
    response = get_url(path, url, force)
    response.html.render(scrolldown=15, sleep=5, timeout=5)
    soup = BeautifulSoup(response.html.raw_html, 'lxml')
    with open(EN_INDEX_DIR_PRE, "w") as file:
        file.write(str(soup))


if __name__ == '__main__':
    retrieve_index(EN_INDEX_DIR_PRE, WEBSITE_URL, force=True)
