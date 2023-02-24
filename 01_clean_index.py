from bs4 import BeautifulSoup
from utils import get_url, parse_href
from config import ENGLISH_SUBDIR, EN_INDEX_DIR_PRE, EN_INDEX_DIR, JS_DIR
import os
from urllib.parse import urljoin

if __name__ == '__main__':
    with open(EN_INDEX_DIR_PRE, 'rb') as f:
        soup = BeautifulSoup(f, features='lxml')
        link_id = 0
        links = soup.find_all('a')
        for link in links:
            if hasattr(link, 'href'):
                subpage_name = f'subpage-{link_id}.html'
                destination = os.path.join(ENGLISH_SUBDIR, subpage_name)
                href = parse_href(link.get('href'))
                res = get_url(destination, href)
                if res and res.status_code == 200:
                    new_href = os.path.join('subpages', subpage_name)
                    link['href'] = new_href
                link_id += 1
        scripts = soup.find_all('script')
        for i, script in enumerate(scripts):
            if not script.string:
                continue
            script_path = os.path.join(JS_DIR, f"{i}.js")
            if not os.path.exists(script_path):
                with open(script_path, "w") as file:
                    file.write(script.text)
            new_script = soup.new_tag('script',
                                      attrs={
                                          'defer': None,
                                          'src': script_path,
                                          'type': 'text/javascript'
                                      })
            script.replace_with(new_script)
        with open(EN_INDEX_DIR, "w") as file:
            file.write(str(soup))
