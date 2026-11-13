#!/bin/sh
# Render the SVG artwork to a PNG with headless Chrome.
#   sh art/render.sh
# Writes art/sun-thief.svg, art/render.html, art/sun-thief.png and
# art/sun-thief-final.png (the 1024x1024 PNG that becomes entry.png).
set -e
ART="$(dirname "$0")"
cd "$ART"

python3 gen_sun_thief.py

python3 - <<'PY'
svg = open('sun-thief.svg').read()
html = ('<!doctype html><html><head><meta charset="utf-8"><style>'
        'html,body{margin:0;padding:0;background:#000;width:1024px;height:1024px;overflow:hidden}'
        'svg{display:block}</style></head><body>' + svg + '</body></html>')
open('render.html', 'w').write(html)
PY

google-chrome --headless=new --disable-gpu --no-sandbox --disable-dev-shm-usage \
  --user-data-dir=/tmp/opencode/chrome-prof --hide-scrollbars --force-device-scale-factor=1 \
  --window-size=1024,1024 --screenshot=sun-thief.png "file://$ART/render.html" 2>/dev/null

python3 - <<'PY'
from PIL import Image
im = Image.open('sun-thief.png')
print('rendered', im.size, im.mode)
im.convert('RGB').save('sun-thief-final.png', optimize=True)
import os
print('png bytes', os.path.getsize('sun-thief-final.png'))
PY
