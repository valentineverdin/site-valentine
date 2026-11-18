"""Reconstruit un site statique propre à partir du template extrait du bundle."""
import os, re, shutil

SRC = 'extracted/_template.html'
OUT = 'site'
IMG_UUID = '25cd11eb-1ef8-4c70-98de-33c83962f7e3'

t = open(SRC, encoding='utf-8').read()

# 1. Retirer le runtime du bundler et les métas du canvas de design.
t = t.replace('<script src="a21e095b-86e0-4d8c-8b68-cbc2aaa941b1"></script>\n', '')
t = re.sub(r'<meta name="hz:[^>]*>', '', t)
t = re.sub(r'\s*<script type="text/x-dc".*?</script>', '', t, flags=re.S)

# 2. Retirer les attributs et balises propres à l'outil de maquette.
t = re.sub(r'\s+data-(canvas-width|canvas-height|document-role|label)="[^"]*"', '', t)
t = re.sub(r'</?x-dc>\n?', '', t)
t = re.sub(r'</?helmet>\n?', '', t)

# 3. Le bundler avait renommé les attributs camelCase du SVG.
t = t.replace('sc-camel-view-box=', 'viewBox=')

# 4. Polices : remplacer le bloc @font-face (woff2 embarqué + gstatic) par Google Fonts.
first_style = t.find('<style>')
end_style = t.find('</style>', first_style) + len('</style>')
assert '@font-face' in t[first_style:end_style], 'bloc @font-face introuvable'
t = t[:first_style] + t[end_style:]

head_extra = (
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    '<meta name="description" content="Valentine Verdin, diététicienne-nutritionniste à Bruxelles. '
    'Troubles digestifs (SII, SIBO, IMO), santé de la femme et relation à la nourriture.">\n'
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2'
    '?family=DM+Sans:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap">\n'
    '<link rel="stylesheet" href="styles.css">\n'
)
t = t.replace('<title>', head_extra + '<title>', 1)

# 5. Sortir le CSS restant dans son propre fichier.
m = re.search(r'<style>(.*?)</style>', t, re.S)
css = m.group(1).strip()
t = t[:m.start()] + t[m.end():]

# 6. Image : un vrai fichier au lieu de l'uuid.
t = t.replace('src="%s"' % IMG_UUID, 'src="assets/valentine.jpg"')

# 7. Nettoyer les lignes vides laissées par les suppressions.
t = re.sub(r'\n{3,}', '\n\n', t).strip() + '\n'

os.makedirs(OUT + '/assets', exist_ok=True)
open(OUT + '/index.html', 'w', encoding='utf-8').write(t)
open(OUT + '/styles.css', 'w', encoding='utf-8').write(css + '\n')
shutil.copy('extracted/%s.jpg' % IMG_UUID, OUT + '/assets/valentine.jpg')

print('index.html : %d caracteres' % len(t))
print('styles.css : %d caracteres' % len(css))
print('uuid residuels :', re.findall(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', t) or 'aucun')
print('artefacts residuels :', [p for p in ('x-dc', 'helmet', 'sc-camel-', 'hz:', 'data-canvas') if p in t] or 'aucun')
