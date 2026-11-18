# Site Valentine Verdin

Site vitrine de Valentine Verdin, diététicienne-nutritionniste à Bruxelles —
troubles digestifs (SII, SIBO, IMO), santé de la femme, relation à la nourriture.

Page statique : pas de build, pas de dépendances. On ouvre `index.html` et ça marche.

## Structure

| Chemin | Rôle |
| --- | --- |
| `index.html` | La page d'accueil, 15 sections (header → footer) |
| `styles.css` | Les styles partagés (`.wrap`, `.btn`, `.card`, `.chip`, `.eyebrow`…) |
| `assets/` | Images |
| `source/` | Fichiers de travail, non publiés : l'export d'origine et le script d'extraction |

Les polices (DM Sans, DM Serif Display) sont chargées depuis Google Fonts.

## Voir le site en local

```bash
python3 -m http.server 4173
```

Puis ouvrir http://localhost:4173.

## Reste à faire

- [ ] Remplacer les 3 encarts « Photo à venir »
- [ ] Compléter l'adresse du siège dans le pied de page (`[adresse à confirmer]`)
- [ ] Écrire les mentions légales et la politique de confidentialité (RGPD)
- [ ] Brancher les 7 liens encore en `href="#"` (bascule FR/EN, pages légales, « Demander une intervention »)
- [ ] Version anglaise
