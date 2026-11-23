#!/usr/bin/env python3
"""Contrôle automatique du site avant publication.

Vérifie, sur chaque page :
  • un seul titre H1
  • un titre de page de moins de 60 caractères
  • une description de 140 à 155 caractères
  • une adresse canonique
  • les liens hreflang (fr-BE, en, x-default)
  • des données structurées pour Google
  • un lien de prise de rendez-vous
  • pas de [À COMPLÉTER] resté dans le texte

Sort en erreur (code 1) si un contrôle échoue : la publication est bloquée.
Usage :  python3 verifier.py
"""
import os
import re
import sys
import json

RACINE = os.path.dirname(os.path.abspath(__file__))
IGNORER = {"source", ".git", "node_modules", "dist"}
DESC_MIN, DESC_MAX = 140, 155
TITRE_MAX = 60


def pages():
    for dossier, sous, fichiers in os.walk(RACINE):
        sous[:] = [d for d in sous if d not in IGNORER and not d.startswith(".")]
        for f in sorted(fichiers):
            if f.endswith(".html"):
                yield os.path.join(dossier, f)


def attribut(html, balise, cle, valeur):
    motif = rf'<{balise}[^>]*{cle}=["\']{re.escape(valeur)}["\'][^>]*>'
    return re.search(motif, html, re.I) is not None


def controler(chemin):
    nom = os.path.relpath(chemin, RACINE)
    html = open(chemin, encoding="utf-8").read()
    noindex = re.search(r'<meta[^>]*name=["\']robots["\'][^>]*noindex', html, re.I)
    soucis = []

    # H1 unique
    n_h1 = len(re.findall(r"<h1[\s>]", html, re.I))
    if n_h1 != 1:
        soucis.append(f"{n_h1} titre(s) H1 au lieu d'un seul")

    # Titre
    m = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
    if not m:
        soucis.append("pas de titre de page")
    elif len(m.group(1).strip()) > TITRE_MAX:
        soucis.append(f"titre de {len(m.group(1).strip())} caractères (maximum {TITRE_MAX})")

    # Description
    m = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', html, re.S | re.I)
    if not m:
        soucis.append("pas de description")
    else:
        n = len(m.group(1).strip())
        if not (DESC_MIN <= n <= DESC_MAX):
            soucis.append(f"description de {n} caractères (attendu {DESC_MIN} à {DESC_MAX})")

    # Canonique
    if not attribut(html, "link", "rel", "canonical"):
        soucis.append("pas d'adresse canonique")

    # hreflang — pas exigé sur une page hors index (404, pages légales)
    if not noindex and "mentions-legales" not in nom and "confidentialite" not in nom:
        for code in ("fr-BE", "en", "x-default"):
            if not attribut(html, "link", "hreflang", code):
                soucis.append(f"hreflang {code} manquant")

    # Données structurées
    blocs = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
                       html, re.S | re.I)
    legale = 'mentions-legales' in nom or 'confidentialite' in nom
    if not blocs and not noindex and not legale:
        soucis.append("pas de données structurées")
    for i, b in enumerate(blocs, 1):
        try:
            json.loads(b)
        except json.JSONDecodeError as e:
            soucis.append(f"données structurées n°{i} invalides : {e}")

    # Lien de rendez-vous
    if not noindex and "mentions-legales" not in nom and "confidentialite" not in nom:
        if "doctoranytime" not in html and "rendez-vous/" not in html \
                and "book-an-appointment/" not in html:
            soucis.append("pas de lien de prise de rendez-vous")

    # Texte resté à compléter
    if "À COMPLÉTER" in html:
        soucis.append("un [À COMPLÉTER] est resté dans la page")

    # Images : chaque fichier référencé doit exister
    for src in re.findall(r'<img[^>]*src=["\']([^"\']+)["\']', html, re.I):
        if src.startswith(("http://", "https://", "data:")):
            continue
        if not os.path.isfile(os.path.join(os.path.dirname(chemin), src)):
            soucis.append(f"image introuvable : {src}")

    return nom, soucis


def main():
    total = 0
    en_echec = 0
    for chemin in pages():
        nom, soucis = controler(chemin)
        total += 1
        if soucis:
            en_echec += 1
            print(f"\n  ✗ {nom}")
            for s in soucis:
                print(f"      {s}")
        else:
            print(f"  ✓ {nom}")

    print(f"\n{total} page(s) contrôlée(s), {en_echec} en échec.")
    if en_echec:
        print("\nPublication bloquée : corrigez les points ci-dessus.")
        return 1
    print("Tout est en ordre.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
