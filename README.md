# Site Valentine Verdin

Site de Valentine Verdin, diététicienne-nutritionniste à Bruxelles —
troubles digestifs (SII, SIBO, IMO, ISO), santé de la femme, relation à la
nourriture. En ligne sur **https://www.valentineverdin.be**

Pages statiques : pas de dépendance à installer, Python 3 suffit.

## Structure

| Chemin | Rôle |
| --- | --- |
| `index.html` | Accueil, français |
| `en/index.html` | Accueil, anglais |
| `deroulement-et-tarifs/`, `rendez-vous/`, `contact/` | Pages françaises générées |
| `en/how-it-works-fees/`, `en/book-an-appointment/`, `en/contact/` | Leurs équivalents anglais |
| `mentions-legales.html`, `confidentialite.html` | Pages légales, en français |
| `404.html` | Page d'erreur bilingue |
| `styles.css`, `assets/`, `favicon.svg` | Styles, images, icône |
| `brief.md` | **Source de vérité des contenus** |
| `construire.py` | Génère les pages |
| `verifier.py` | Contrôle avant publication |
| `source/` | Export d'origine de la maquette, non publié |

## Modifier le site

Les textes des pages générées sont dans `construire.py`, en français lisible,
regroupés en haut du fichier. Après toute modification :

```bash
python3 construire.py && python3 verifier.py
```

`construire.py` réécrit les pages. `verifier.py` contrôle chacune d'elles :
un seul titre H1, titre de page sous 60 caractères, description entre 140 et
155, adresse canonique, liens hreflang, données structurées, lien de
rendez-vous, images présentes, et aucun `[À COMPLÉTER]` oublié.

L'accueil (`index.html`, `en/index.html`) et les pages légales sont écrits à
la main : `construire.py` ne les touche pas, mais `verifier.py` les contrôle.

## Voir le site en local

```bash
python3 -m http.server 4173
```

Puis ouvrir http://localhost:4173.

## Publication

Chaque envoi sur `main` déclenche `.github/workflows/publier.yml` :

1. les pages sont regénérées, et le workflow échoue si le résultat diffère
   de ce qui est dans le dépôt ;
2. `verifier.py` contrôle chaque page ;
3. le site n'est publié **que si tout passe**.

Si un contrôle échoue, la version en ligne reste la dernière version valide.

## Reste à faire

- [ ] Pages Troubles digestifs, Santé de la femme et À propos — en attente
      des textes (endométriose, SOPK, ménopause, parcours)
- [ ] Lien de rendez-vous CHIREC pour Delta et Louise
- [ ] Question FAQ sur le Breath test : où, prescription, coût
- [ ] Les 24 `[À COMPLÉTER]` restants de `brief.md`
