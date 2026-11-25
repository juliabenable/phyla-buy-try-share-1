"""Build brand.html: inline production CSS, the Rights tab cs- styles, posters and logo as data URIs."""
import base64, re, pathlib
here = pathlib.Path(__file__).parent; src = here / 'src'
s = (src / 'brand.html').read_text()
s = s.replace('/*@@RIGHTS_CS@@*/', (src / 'rights-cs.css').read_text())
for css in ['newflow-extra.css', 'newflow-production.css']:
    s = s.replace(f'<link rel="stylesheet" href="assets/{css}">', '<style>' + (src / 'assets' / css).read_text() + '</style>')
def uri(name):
    b = (src / 'assets' / name).read_bytes(); mime = 'image/svg+xml' if name.endswith('.svg') else 'image/jpeg'
    return f'data:{mime};base64,' + base64.b64encode(b).decode()
s = s.replace("const A = 'assets/';", 'const IMG = ' + repr({n: uri(n) for n in ['logo.svg','quinn-1.jpg','emery-1.jpg','jasper-1.jpg','quinn-2.jpg','emery-2.jpg']}).replace("'", '"') + ";\nconst A = '';")
s = s.replace("${A}logo.svg", '${IMG["logo.svg"]}')
s = s.replace("av: A + POSTERS[i % POSTERS.length] + '.jpg', poster: A + POSTERS[(i + 2) % POSTERS.length] + '.jpg',",
              "av: IMG[POSTERS[i % POSTERS.length] + '.jpg'], poster: IMG[POSTERS[(i + 2) % POSTERS.length] + '.jpg'],")
assert 'assets/' not in re.sub(r'url\([^)]*\)', '', s.split('<script>')[1]), 'unresolved asset in script'
(here / 'brand.html').write_text(s)
print('brand.html', round(len(s) / 1e6, 2), 'MB')

# ---- creator.html: inline every m/<asset> as a data URI ----
MIME = {'.png': 'image/png', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml'}
c = (src / 'creator.html').read_text()
def inline(m):
    f = src / 'm' / m.group(1)
    return 'data:' + MIME[f.suffix] + ';base64,' + base64.b64encode(f.read_bytes()).decode()
c = re.sub(r'm/([\w.-]+\.(?:png|jpg|svg))', inline, c)
(here / 'creator.html').write_text(c)
print('creator.html', round(len(c) / 1e6, 2), 'MB')

# ---- stickers.html: price sticker options study ----
k = re.sub(r'm/([\w.-]+\.(?:png|jpg|svg))', inline, (src / 'stickers.html').read_text())
(here / 'stickers.html').write_text(k)
print('stickers.html', round(len(k) / 1e6, 2), 'MB')

# ---- creator-v2.html: Nov 25 designs ----
v = re.sub(r'm/([\w.-]+\.(?:png|jpg|svg))', inline, (src / 'creator-v2.html').read_text())
(here / 'creator-v2.html').write_text(v)
print('creator-v2.html', round(len(v) / 1e6, 2), 'MB')

# ---- tiles.html: campaign tile options study ----
t = re.sub(r'm/([\w.-]+\.(?:png|jpg|svg))', inline, (src / 'tiles.html').read_text())
(here / 'tiles.html').write_text(t)
print('tiles.html', round(len(t) / 1e6, 2), 'MB')
