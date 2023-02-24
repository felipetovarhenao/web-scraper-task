from utils import translate_html
from config import HINDI_SUBDIR, ENGLISH_SUBDIR
import os

backends = [
    'google',
    'bing',
    'niutrans',
    'iciba',
]

for i, sp in enumerate(sorted(os.listdir(ENGLISH_SUBDIR))):
    backend = backends[i % len(backends)]
    in_path = os.path.join(ENGLISH_SUBDIR, sp)
    out_path = os.path.join(HINDI_SUBDIR, sp)
    translate_html(in_path, out_path, backend=backend)
