#!/usr/bin/env python3
"""Fabrique les pages du site à partir des contenus ci-dessous.

Usage :  python3 construire.py
Puis  :  python3 verifier.py

L'en-tête, le pied de page et les métadonnées sont écrits une seule fois,
ici. Les textes de chaque page sont dans la section CONTENUS, en français
lisible, séparés du code de mise en page.
"""
import os

RACINE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.valentineverdin.be"
RDV = "https://www.doctoranytime.be/d/dieteticien/verdin-valentine"
ROSA = "https://rosa.be/fr/hp/valentine-verdin-1/"

# ---------------------------------------------------------------- identité
IDENTITE = {
    "societe": "VVERDIN DIET SRL",
    "bce": "1037.780.531",
    "agrement": "28349",
    "inami": "5 62 413 90 601",
    "siege": "Avenue Clémentine 39, 1060 Bruxelles",
    "email": "vverdin.diet@gmail.com",
    "tel": "+32 473 34 15 27",
    "tel_lien": "+32473341527",
}

LIEUX = [
    ("CHIREC — Hôpital Delta", "Boulevard du Triomphe 201, 1160 Auderghem",
     "CHIREC Delta"),
    ("City Clinic Louise", "Avenue Louise 235b, 1050 Ixelles", "City Clinic Louise"),
    ("Uccle — CEDAD Medical Center", "Rue Beeckman 71, 1180 Uccle", "CEDAD Uccle"),
]

TARIFS = [("15 minutes", "appel téléphonique ou vidéo", "40 €"),
          ("30 minutes", "consultation de suivi", "80 €"),
          ("45 minutes", "consultation longue", "100 €"),
          ("60 minutes", "bilan initial", "120 €")]

TARIFS_EN = [("15 minutes", "phone or video call", "€40"),
             ("30 minutes", "follow-up consultation", "€80"),
             ("45 minutes", "long consultation", "€100"),
             ("60 minutes", "initial assessment", "€120")]

# ---------------------------------------------------------------- gabarits
def tete(lang, titre, description, chemin, jumelle, profondeur, extra=""):
    """<head> complet. `profondeur` = nombre de dossiers à remonter."""
    haut = "../" * profondeur
    canon = f"{SITE}{chemin}"
    fr = canon if lang == "fr" else f"{SITE}{jumelle}"
    en = f"{SITE}{jumelle}" if lang == "fr" else canon
    og = "og-valentine-verdin.jpg" if lang == "fr" else "og-valentine-verdin-en.jpg"
    locale = "fr_BE" if lang == "fr" else "en_GB"
    autre = "en_GB" if lang == "fr" else "fr_BE"
    return f"""<!DOCTYPE html>
<html lang="{lang}"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="fr-BE" href="{fr}">
<link rel="alternate" hreflang="fr" href="{fr}">
<link rel="alternate" hreflang="en" href="{en}">
<link rel="alternate" hreflang="x-default" href="{fr}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{locale}">
<meta property="og:locale:alternate" content="{autre}">
<meta property="og:site_name" content="Valentine Verdin">
<meta property="og:url" content="{canon}">
<meta property="og:title" content="{titre}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{SITE}/assets/{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{haut}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display:ital@0;1&display=swap">
<link rel="stylesheet" href="{haut}styles.css">
{extra}</head>
<body>
"""


def entete(lang, profondeur, jumelle):
    haut = "../" * profondeur
    if lang == "fr":
        liens = [(f"{haut}#digestif", "Troubles digestifs"),
                 (f"{haut}#femme", "Santé de la femme"),
                 (f"{haut}#methode", "Ma méthode"),
                 (f"{haut}deroulement-et-tarifs/", "Déroulement et tarifs"),
                 (f"{haut}rendez-vous/", "Prendre rendez-vous")]
        sous = "Diététicienne · Nutritionniste"
        bouton, autre_lang, aria = "Prendre rendez‑vous", "EN", "View this site in English"
    else:
        liens = [(f"{haut}#digestif", "Gut health"),
                 (f"{haut}#femme", "Women's health"),
                 (f"{haut}#methode", "My method"),
                 (f"{haut}how-it-works-fees/", "How it works &amp; fees"),
                 (f"{haut}book-an-appointment/", "Book an appointment")]
        sous = "Dietitian · Nutritionist"
        bouton, autre_lang, aria = "Book an appointment", "FR", "Voir ce site en français"
    nav = "\n      ".join(f'<a class="navlink" href="{u}">{t}</a>' for u, t in liens)
    rdv = f"{haut}rendez-vous/" if lang == "fr" else f"{haut}book-an-appointment/"
    return f"""<header style="width:100%;background:#F6F1E9;border-bottom:1px solid #E2DAC8">
  <div class="wrap" style="display:flex;flex-wrap:wrap;align-items:center;gap:1rem 2rem;padding-top:1.1rem;padding-bottom:1.1rem">
    <a href="{haut}" style="display:flex;flex-direction:column;line-height:1.05;margin-right:auto">
      <span style="font-family:'DM Serif Display',Georgia,serif;font-size:1.45rem">Valentine Verdin</span>
      <span style="font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;color:#8A7E6B;font-weight:600;margin-top:.2rem">{sous}</span>
    </a>
    <nav aria-label="Navigation" style="display:flex;flex-wrap:wrap;gap:1.4rem;align-items:center">
      {nav}
    </nav>
    <div style="display:flex;align-items:center;gap:1.2rem">
      <a href="{SITE}{jumelle}" aria-label="{aria}" class="navlink" style="font-weight:600;color:#2F3A33">{autre_lang}</a>
      <a href="{rdv}" class="btn btn-primary">{bouton}</a>
    </div>
  </div>
</header>
"""


def pied(lang, profondeur):
    haut = "../" * profondeur
    i = IDENTITE
    if lang == "fr":
        metier = "Diététicienne‑nutritionniste · troubles digestifs &amp; santé de la femme"
        titres = ("Navigation", "Contact")
        liens = [(f"{haut}deroulement-et-tarifs/", "Déroulement et tarifs"),
                 (f"{haut}rendez-vous/", "Prendre rendez-vous"),
                 (f"{haut}contact/", "Contact")]
        legal = (f'<a href="{haut}mentions-legales.html" style="color:#B9C1B4;text-decoration:underline">Mentions légales</a> · '
                 f'<a href="{haut}confidentialite.html" style="color:#B9C1B4;text-decoration:underline">Politique de confidentialité (RGPD)</a>')
        mentions = (f"{i['societe']} · BCE {i['bce']} · N° d'agrément diététicien {i['agrement']} · "
                    f"INAMI {i['inami']} · Siège : {i['siege']} · {legal} · © 2026")
    else:
        metier = "Dietitian‑nutritionist · digestive disorders &amp; women's health"
        titres = ("Navigation", "Contact")
        liens = [(f"{haut}how-it-works-fees/", "How it works &amp; fees"),
                 (f"{haut}book-an-appointment/", "Book an appointment"),
                 (f"{haut}contact/", "Contact")]
        legal = (f'<a href="{SITE}/mentions-legales.html" hreflang="fr" lang="fr" style="color:#B9C1B4;text-decoration:underline">Mentions légales (in French)</a> · '
                 f'<a href="{SITE}/confidentialite.html" hreflang="fr" lang="fr" style="color:#B9C1B4;text-decoration:underline">Privacy policy (in French)</a>')
        mentions = (f"{i['societe']} · Company number {i['bce']} · Dietitian registration {i['agrement']} · "
                    f"INAMI {i['inami']} · Registered office: {i['siege']} · {legal} · © 2026")
    nav = "\n        ".join(
        f'<p style="margin:.3rem 0"><a href="{u}" style="color:#C7BFB0">{t}</a></p>' for u, t in liens)
    return f"""<footer style="width:100%;background:#2F3A33;color:#C7BFB0">
  <div class="wrap" style="padding-top:clamp(2.5rem,5vw,4rem);padding-bottom:2.5rem">
    <div style="display:flex;flex-wrap:wrap;gap:2rem 3rem;justify-content:space-between">
      <div style="flex:1 1 280px;min-width:0">
        <p style="font-family:'DM Serif Display',Georgia,serif;font-size:1.4rem;color:#F6F1E9">Valentine Verdin</p>
        <p style="margin-top:.4rem;font-size:.9rem">{metier}</p>
      </div>
      <div style="flex:1 1 180px;min-width:0">
        <p style="color:#9FA79B;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;margin-bottom:.8rem">{titres[0]}</p>
        {nav}
      </div>
      <div style="flex:1 1 220px;min-width:0">
        <p style="color:#9FA79B;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;margin-bottom:.8rem">{titres[1]}</p>
        <p style="margin:.3rem 0;font-size:.9rem"><a href="mailto:{i['email']}" style="color:#C7BFB0">{i['email']}</a></p>
        <p style="margin:.3rem 0;font-size:.9rem"><a href="tel:{i['tel_lien']}" style="color:#C7BFB0">{i['tel']}</a></p>
      </div>
    </div>
    <hr style="border:none;border-top:1px solid #45544A;margin:2.2rem 0 1.4rem">
    <p style="font-size:.78rem;color:#8E978B;line-height:1.8">{mentions}</p>
  </div>
</footer>
</body></html>
"""


def barre_mobile(lang, profondeur):
    """Bouton de rendez-vous fixé en bas de l'écran, sur téléphone uniquement."""
    haut = "../" * profondeur
    cible = f"{haut}rendez-vous/" if lang == "fr" else f"{haut}book-an-appointment/"
    texte = "Prendre rendez‑vous" if lang == "fr" else "Book an appointment"
    return f"""<div class="barre-rdv"><a href="{cible}" class="btn btn-primary" style="width:100%;justify-content:center">{texte}</a></div>
"""


def bloc_json(contenu):
    return f'<script type="application/ld+json">\n{contenu}\n</script>\n'


# ---------------------------------------------------------------- contenus
def tableau_tarifs(tarifs, entetes):
    lignes = "\n".join(
        f'        <tr><td style="padding:.85rem 1rem;border-bottom:1px solid #E6DECB">{d}</td>'
        f'<td style="padding:.85rem 1rem;border-bottom:1px solid #E6DECB;color:#4A544C">{q}</td>'
        f'<td style="padding:.85rem 1rem;border-bottom:1px solid #E6DECB;font-weight:600;text-align:right">{p}</td></tr>'
        for d, q, p in tarifs)
    return f"""<table style="width:100%;border-collapse:collapse;max-width:620px;margin-top:1.5rem">
      <thead><tr>
        <th scope="col" style="text-align:left;padding:.6rem 1rem;font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:#8A7E6B">{entetes[0]}</th>
        <th scope="col" style="text-align:left;padding:.6rem 1rem;font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:#8A7E6B">{entetes[1]}</th>
        <th scope="col" style="text-align:right;padding:.6rem 1rem;font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:#8A7E6B">{entetes[2]}</th>
      </tr></thead>
      <tbody>
{lignes}
      </tbody>
    </table>"""


FAQ_FR = [
    ("Combien coûte une consultation ?",
     "Le tarif dépend uniquement de la durée : 40 € pour 15 minutes, 80 € pour 30 minutes, "
     "100 € pour 45 minutes et 120 € pour le bilan initial d'une heure. La visioconsultation "
     "suit exactement la même grille."),
    ("Suis-je remboursée par ma mutuelle ?",
     "En partie. Le montant varie d'une mutuelle à l'autre et peut aller jusqu'à 25 € par "
     "consultation. Je suis non-conventionnée : le remboursement passe par votre assurance "
     "complémentaire. Je vous remets une attestation de soin à chaque consultation, c'est elle "
     "qui vous permet de vous faire rembourser."),
    ("Faut-il une prescription de mon médecin ?",
     "Non, elle n'est pas obligatoire pour me consulter. Elle reste utile : avec une "
     "prescription, votre mutuelle rembourse en général davantage de séances — entre 4 et 8 par an."),
    ("Consultez-vous en visioconsultation ?",
     "Oui, depuis le monde entier, en français, en anglais et en italien. Le tarif est le même "
     "qu'en présentiel."),
    ("Combien de temps dure le suivi ?",
     "Cela dépend de votre situation. Parfois, une seule consultation suffit à débloquer les "
     "choses. Le plus souvent, comptez 3 à 5 rendez-vous : mon objectif est de vous rendre "
     "autonome le plus rapidement possible."),
    ("Où se déroulent les consultations ?",
     "À trois adresses bruxelloises : le CHIREC — Hôpital Delta (Boulevard du Triomphe 201, "
     "1160 Auderghem), la City Clinic Louise (Avenue Louise 235b, 1050 Ixelles) et le CEDAD "
     "Medical Center à Uccle (Rue Beeckman 71, 1180 Uccle). Et en visioconsultation."),
    ("Le Low FODMAP, est-ce un régime à vie ?",
     "Non, surtout pas. Le protocole se déroule en trois phases : une éviction d'environ quatre "
     "semaines, puis une réintroduction guidée famille d'aliments par famille d'aliments, et "
     "enfin votre alimentation personnalisée, durable, la plus large possible."),
    ("Comment puis-je payer, et que se passe-t-il si j'annule ?",
     "Le paiement se fait en espèces ou par QR code. Pour les annulations : sans frais au-delà "
     "de 48 heures, 50 % du montant entre 48 et 24 heures, et la séance est due en totalité en "
     "deçà de 24 heures ou en cas d'absence non justifiée."),
]

FAQ_EN = [
    ("How much does a consultation cost?",
     "The fee depends only on the length: €40 for 15 minutes, €80 for 30 minutes, €100 for 45 "
     "minutes and €120 for the one-hour initial assessment. Online consultations follow exactly "
     "the same scale."),
    ("Will my health insurance reimburse me?",
     "Partly. The amount varies between Belgian mutuelles and can go up to €25 per consultation. "
     "I am not conventionné, so reimbursement goes through your complementary insurance. I give "
     "you a care certificate at every consultation — that is the document you claim with."),
    ("Do I need a referral from my doctor?",
     "No, a referral is not required to see me. It is still useful: with one, your mutuelle "
     "usually reimburses more sessions — typically between four and eight a year."),
    ("Do you consult online?",
     "Yes, from anywhere in the world, in English, French or Italian. The fee is the same as "
     "for an in-person consultation."),
    ("How long does the follow-up last?",
     "It depends on your situation. Sometimes a single consultation is enough to unlock things. "
     "More often, expect three to five appointments: my aim is to make you independent as "
     "quickly as possible."),
    ("Where do consultations take place?",
     "At three addresses in Brussels: CHIREC — Delta Hospital (Boulevard du Triomphe 201, 1160 "
     "Auderghem), City Clinic Louise (Avenue Louise 235b, 1050 Ixelles) and the CEDAD Medical "
     "Center in Uccle (Rue Beeckman 71, 1180 Uccle). And online."),
    ("Is Low FODMAP a diet for life?",
     "No — quite the opposite. The protocol runs in three phases: roughly four weeks of "
     "elimination, then a guided reintroduction food group by food group, and finally your own "
     "personalised, sustainable and as varied as possible way of eating."),
    ("How do I pay, and what happens if I cancel?",
     "Payment is by cash or QR code. For cancellations: free of charge more than 48 hours "
     "ahead, 50% of the fee between 48 and 24 hours, and the full fee under 24 hours or if you "
     "do not attend."),
]


def faq_html(questions, titre):
    items = "\n".join(
        f"""      <div style="border-top:1px solid #E6DECB;padding:1.4rem 0">
        <h3 style="margin:0 0 .6rem;font-size:1.15rem">{q}</h3>
        <p style="color:#4A544C;line-height:1.7;margin:0">{r}</p>
      </div>""" for q, r in questions)
    return f"""<section style="width:100%;background:#F6F1E9">
  <div class="wrap sct">
    <h2 style="margin:0 0 1.8rem;font-size:clamp(1.8rem,3.2vw,2.4rem)">{titre}</h2>
    <div style="max-width:760px">
{items}
    </div>
  </div>
</section>
"""


def faq_donnees(questions):
    import json
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in questions]
    }, ensure_ascii=False, indent=2)


def donnees_lieu(lang):
    import json
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "MedicalBusiness",
        "@id": f"{SITE}/#cabinet",
        "name": "Valentine Verdin — " + ("Diététicienne-nutritionniste" if lang == "fr"
                                         else "Dietitian-nutritionist"),
        "url": SITE + ("/" if lang == "fr" else "/en/"),
        "email": IDENTITE["email"],
        "telephone": IDENTITE["tel"],
        "priceRange": "€€",
        "availableLanguage": ["fr", "en", "it"],
        "areaServed": {"@type": "City", "name": "Bruxelles"},
        "medicalSpecialty": "Dietetics",
        "location": [
            {"@type": "Place", "name": nom,
             "address": {"@type": "PostalAddress", "streetAddress": adr,
                         "addressLocality": "Bruxelles", "addressCountry": "BE"}}
            for nom, adr, _ in LIEUX],
    }, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------- pages
def page_tarifs(lang):
    if lang == "fr":
        chemin, jumelle = "/deroulement-et-tarifs/", "/en/how-it-works-fees/"
        titre = "Tarifs et déroulement — Diététicienne à Bruxelles"
        desc = ("Tarifs, remboursement mutuelle et déroulement du suivi chez Valentine Verdin, "
                "diététicienne-nutritionniste à Bruxelles. De 40 à 120 € selon la durée.")
        h1 = "Déroulement et tarifs"
        intro = ("Tout est annoncé à l'avance : ce que coûte une consultation, ce que votre "
                 "mutuelle vous rembourse, et comment se déroule le suivi. Aucune surprise.")
        t_tarifs, entetes = TARIFS, ("Durée", "Type de consultation", "Tarif")
        faq, titre_faq = FAQ_FR, "Questions fréquentes"
    else:
        chemin, jumelle = "/en/how-it-works-fees/", "/deroulement-et-tarifs/"
        titre = "Fees and how it works — Dietitian in Brussels"
        desc = ("Fees, health insurance reimbursement and how the follow-up works with Valentine "
                "Verdin, English-speaking dietitian in Brussels. From €40 to €120.")
        h1 = "How it works &amp; fees"
        intro = ("Everything is stated upfront: what a consultation costs, what your mutuelle "
                 "reimburses, and how the follow-up runs. No surprises.")
        t_tarifs, entetes = TARIFS_EN, ("Length", "Type of consultation", "Fee")
        faq, titre_faq = FAQ_EN, "Frequently asked questions"

    prof = 1 if lang == "fr" else 2
    etapes_fr = [
        ("Bilan initial · 60 min",
         "Votre histoire, vos symptômes, vos examens. On fait le point ensemble, en lien avec votre médecin."),
        ("Plan sur mesure",
         "Besoin d'un cadre précis — nutrition du sport, objectif de perte de poids ? Je construis un plan tenant compte de vos goûts et de vos aversions."),
        ("Personnalisation",
         "Un service de consultance : on travaille ce dont vous avez besoin — coaching motivationnel, liste de courses, ou tout autre appui utile."),
        ("Lien avec votre médecin",
         "Un courrier de suivi adressé à votre médecin après chaque bilan."),
    ]
    etapes_en = [
        ("Initial assessment · 60 min",
         "Your history, your symptoms, your test results. We take stock together, in contact with your doctor."),
        ("A tailored plan",
         "Need a precise framework — sports nutrition, a weight-loss goal? I build a plan around your tastes and your dislikes."),
        ("Personalisation",
         "A consultancy service: we work on what you actually need — motivational coaching, a shopping list, or any other support."),
        ("Link with your doctor",
         "A follow-up letter sent to your doctor after every assessment."),
    ]
    etapes = etapes_fr if lang == "fr" else etapes_en
    t_etapes = "Comment se passe le suivi" if lang == "fr" else "How the follow-up works"
    t_duree = ("Parfois, une seule consultation suffit à débloquer la situation. Le plus souvent, "
               "comptez 3 à 5 rendez-vous." if lang == "fr" else
               "Sometimes a single consultation is enough to unlock things. More often, expect "
               "three to five appointments.")
    t_rdv = "Prendre rendez‑vous" if lang == "fr" else "Book an appointment"
    cartes = "\n".join(
        f"""      <div style="flex:1 1 240px;min-width:0;border-top:2px solid #C77B58;padding-top:1.1rem">
        <p style="font-weight:600;margin-bottom:.4rem">{t}</p>
        <p style="color:#4A544C;line-height:1.65;font-size:.95rem;margin:0">{d}</p>
      </div>""" for t, d in etapes)

    extra = bloc_json(faq_donnees(faq)) + bloc_json(donnees_lieu(lang))
    rdv_cible = "../rendez-vous/" if lang == "fr" else "../book-an-appointment/"
    html = tete(lang, titre, desc, chemin, jumelle, prof, extra)
    html += entete(lang, prof, jumelle)
    html += f"""<main>
<section style="width:100%;background:#F6F1E9">
  <div class="wrap sct">
    <h1 style="margin:0;font-size:clamp(2rem,4.2vw,3.2rem)">{h1}</h1>
    <p class="lede" style="margin-top:1.2rem;max-width:62ch">{intro}</p>
  </div>
</section>

<section style="width:100%;background:#FBF8F1;border-top:1px solid #E6DECB">
  <div class="wrap sct">
    <h2 style="margin:0;font-size:clamp(1.8rem,3.2vw,2.4rem)">{'Tarifs' if lang == 'fr' else 'Fees'}</h2>
    {tableau_tarifs(t_tarifs, entetes)}
    <p style="margin-top:1.4rem;color:#4A544C;max-width:62ch;line-height:1.7">{t_duree}</p>
  </div>
</section>

<section style="width:100%;background:#2F3A33;color:#F2ECDF">
  <div class="wrap sct">
    <h2 style="margin:0 0 2rem;font-size:clamp(1.8rem,3.2vw,2.4rem);color:#F6F1E9">{t_etapes}</h2>
    <div style="display:flex;flex-wrap:wrap;gap:1.5rem">
{cartes.replace('color:#4A544C', 'color:#C7BFB0')}
    </div>
    <a href="{rdv_cible}" class="btn btn-primary" style="margin-top:2.4rem;background:#E0A684;color:#2F3A33">{t_rdv}</a>
  </div>
</section>

{faq_html(faq, titre_faq)}
</main>
{barre_mobile(lang, prof)}"""
    html += pied(lang, prof)
    return chemin, html


def page_rdv(lang):
    if lang == "fr":
        chemin, jumelle = "/rendez-vous/", "/en/book-an-appointment/"
        titre = "Prendre rendez-vous — Diététicienne à Bruxelles"
        desc = ("Prenez rendez-vous avec Valentine Verdin, diététicienne-nutritionniste à "
                "Bruxelles : Delta, Louise, Uccle ou en visioconsultation, en FR, EN et IT.")
        h1 = "Où souhaitez-vous consulter ?"
        intro = ("Trois adresses à Bruxelles, et la visioconsultation depuis le monde entier. "
                 "Choisissez le lieu qui vous arrange.")
        visio = ("Visioconsultation", "Depuis le monde entier, en français, en anglais ou en italien.")
        bouton = "Prendre rendez‑vous"
    else:
        chemin, jumelle = "/en/book-an-appointment/", "/rendez-vous/"
        titre = "Book an appointment — Dietitian in Brussels"
        desc = ("Book with Valentine Verdin, English-speaking dietitian in Brussels: Delta, "
                "Louise, Uccle or online from anywhere in the world, in English or French.")
        h1 = "Where would you like to be seen?"
        intro = ("Three addresses in Brussels, and online consultations from anywhere in the "
                 "world. Pick whichever suits you.")
        visio = ("Online consultation", "From anywhere in the world, in English, French or Italian.")
        bouton = "Book an appointment"

    prof = 1 if lang == "fr" else 2
    cartes = []
    for nom, adr, _ in LIEUX:
        cartes.append(f"""      <article class="card" style="flex:1 1 300px;min-width:0">
        <h2 style="margin:0;font-size:1.3rem">{nom}</h2>
        <p style="color:#4A544C;line-height:1.6;margin:0">{adr}</p>
        <a href="{RDV}" class="btn btn-primary" style="margin-top:auto" rel="noopener" target="_blank">{bouton}</a>
      </article>""")
    cartes.append(f"""      <article class="card" style="flex:1 1 300px;min-width:0;border-top:3px solid #8FA68E">
        <h2 style="margin:0;font-size:1.3rem">{visio[0]}</h2>
        <p style="color:#4A544C;line-height:1.6;margin:0">{visio[1]}</p>
        <a href="{RDV}" class="btn btn-primary" style="margin-top:auto" rel="noopener" target="_blank">{bouton}</a>
      </article>""")

    autre = ("Vous pouvez aussi passer par Rosa pour les sites Delta et Louise."
             if lang == "fr" else
             "You can also book through Rosa for the Delta and Louise sites.")
    extra = bloc_json(donnees_lieu(lang))
    html = tete(lang, titre, desc, chemin, jumelle, prof, extra)
    html += entete(lang, prof, jumelle)
    html += f"""<main>
<section style="width:100%;background:#F6F1E9">
  <div class="wrap sct">
    <h1 style="margin:0;font-size:clamp(2rem,4.2vw,3.2rem)">{h1}</h1>
    <p class="lede" style="margin-top:1.2rem;max-width:62ch">{intro}</p>
    <div style="margin-top:2.6rem;display:flex;flex-wrap:wrap;gap:1.5rem">
{chr(10).join(cartes)}
    </div>
    <p style="margin-top:2rem;color:#4A544C;font-size:.95rem">{autre} <a href="{ROSA}" rel="noopener" target="_blank" style="text-decoration:underline">Rosa</a></p>
  </div>
</section>
</main>
{barre_mobile(lang, prof)}"""
    html += pied(lang, prof)
    return chemin, html


def page_contact(lang):
    i = IDENTITE
    if lang == "fr":
        chemin, jumelle = "/contact/", "/en/contact/"
        titre = "Contact — Valentine Verdin, diététicienne à Bruxelles"
        desc = ("Contactez Valentine Verdin, diététicienne-nutritionniste à Bruxelles : "
                "e-mail, téléphone et trois adresses de consultation, à Delta, Louise et Uccle.")
        h1 = "Me contacter"
        intro = ("Pour une question d'organisation, une demande d'intervention en entreprise ou "
                 "toute autre question. Pour un rendez-vous, passez plutôt par l'agenda en ligne.")
        t_adr, t_coord, t_rdv = "Adresses de consultation", "Coordonnées", "Prendre rendez‑vous"
        t_langues = "Langues : français, anglais, italien."
    else:
        chemin, jumelle = "/en/contact/", "/contact/"
        titre = "Contact — Valentine Verdin, dietitian in Brussels"
        desc = ("Contact Valentine Verdin, English-speaking dietitian in Brussels: email, phone "
                "and three consultation addresses, at Delta, Louise and Uccle.")
        h1 = "Get in touch"
        intro = ("For a practical question, a request for a workplace talk, or anything else. "
                 "For an appointment, please use the online diary instead.")
        t_adr, t_coord, t_rdv = "Consultation addresses", "Contact details", "Book an appointment"
        t_langues = "Languages: English, French, Italian."

    prof = 1 if lang == "fr" else 2
    adresses = "\n".join(
        f'      <p style="margin:.5rem 0;line-height:1.7"><strong>{nom}</strong><br>{adr}</p>'
        for nom, adr, _ in LIEUX)
    rdv_cible = "../rendez-vous/" if lang == "fr" else "../book-an-appointment/"
    extra = bloc_json(donnees_lieu(lang))
    html = tete(lang, titre, desc, chemin, jumelle, prof, extra)
    html += entete(lang, prof, jumelle)
    html += f"""<main>
<section style="width:100%;background:#F6F1E9">
  <div class="wrap sct">
    <h1 style="margin:0;font-size:clamp(2rem,4.2vw,3.2rem)">{h1}</h1>
    <p class="lede" style="margin-top:1.2rem;max-width:62ch">{intro}</p>
    <div style="margin-top:2.6rem;display:flex;flex-wrap:wrap;gap:2.5rem">
      <div style="flex:1 1 280px;min-width:0">
        <p class="eyebrow" style="margin-bottom:1rem">{t_coord}</p>
        <p style="margin:.5rem 0;font-size:1.05rem"><a href="mailto:{i['email']}" style="text-decoration:underline">{i['email']}</a></p>
        <p style="margin:.5rem 0;font-size:1.05rem"><a href="tel:{i['tel_lien']}" style="text-decoration:underline">{i['tel']}</a></p>
        <p style="margin:1rem 0 0;color:#4A544C">{t_langues}</p>
        <a href="{rdv_cible}" class="btn btn-primary" style="margin-top:1.6rem">{t_rdv}</a>
      </div>
      <div style="flex:1 1 320px;min-width:0">
        <p class="eyebrow" style="margin-bottom:1rem">{t_adr}</p>
{adresses}
      </div>
    </div>
  </div>
</section>
</main>
{barre_mobile(lang, prof)}"""
    html += pied(lang, prof)
    return chemin, html


def page_404():
    titre = "Page introuvable — Valentine Verdin"
    desc = ("Cette page n'existe pas, ou bien elle a été déplacée. Retournez à l'accueil du site de "
            "Valentine Verdin, diététicienne-nutritionniste à Bruxelles.")
    html = tete("fr", titre, desc, "/404.html", "/en/", 0,
                '<meta name="robots" content="noindex">\n')
    html += entete("fr", 0, "/en/")
    html += """<main>
<section style="width:100%;background:#F6F1E9">
  <div class="wrap sct">
    <h1 style="margin:0;font-size:clamp(2rem,4.2vw,3.2rem)">Cette page n'existe pas</h1>
    <p class="lede" style="margin-top:1.2rem;max-width:58ch">Le lien est peut-être erroné, ou la page a été déplacée.<br><span lang="en">This page does not exist. The link may be wrong, or the page has moved.</span></p>
    <div style="margin-top:2rem;display:flex;flex-wrap:wrap;gap:.9rem">
      <a href="/" class="btn btn-primary">Retour à l'accueil</a>
      <a href="/en/" class="btn btn-ghost" hreflang="en" lang="en">Back to the English home page</a>
      <a href="/rendez-vous/" class="btn btn-ghost">Prendre rendez‑vous</a>
    </div>
  </div>
</section>
</main>
"""
    html += pied("fr", 0)
    return "/404.html", html


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#2F3A33"/>
  <text x="32" y="44" font-family="Georgia, serif" font-size="34" fill="#F6F1E9"
        text-anchor="middle">V</text>
</svg>
"""

CSS_BARRE = """
/* Bouton de rendez-vous fixé en bas de l'écran, sur téléphone uniquement. */
.barre-rdv{display:none}
@media (max-width:640px){
  .barre-rdv{display:block;position:fixed;left:0;right:0;bottom:0;z-index:50;
    padding:.7rem 1rem calc(.7rem + env(safe-area-inset-bottom));
    background:rgba(246,241,233,.96);border-top:1px solid #E2DAC8}
  body{padding-bottom:5rem}
}
"""


def sitemap(chemins):
    urls = "\n".join(
        f"  <url><loc>{SITE}{c}</loc></url>" for c in chemins)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.w3.org/1999/xhtml/sitemap/0.9" '
            'xmlns:default="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}\n</urlset>\n")


def ecrire(chemin, contenu):
    if chemin.endswith(".html") and not chemin.endswith("/404.html"):
        dest = os.path.join(RACINE, chemin.lstrip("/"))
    elif chemin.endswith("/"):
        dest = os.path.join(RACINE, chemin.strip("/"), "index.html")
    else:
        dest = os.path.join(RACINE, chemin.lstrip("/"))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8").write(contenu)
    return dest


def main():
    produites = []
    for fabrique in (page_tarifs, page_rdv, page_contact):
        for lang in ("fr", "en"):
            chemin, html = fabrique(lang)
            produites.append((chemin, ecrire(chemin, html)))
    chemin, html = page_404()
    produites.append((chemin, ecrire(chemin, html)))

    open(os.path.join(RACINE, "favicon.svg"), "w", encoding="utf-8").write(FAVICON)

    css = os.path.join(RACINE, "styles.css")
    contenu = open(css, encoding="utf-8").read()
    if ".barre-rdv" not in contenu:
        open(css, "a", encoding="utf-8").write(CSS_BARRE)

    for chemin, dest in produites:
        print(f"  {chemin:36s} -> {os.path.relpath(dest, RACINE)}")
    print(f"\n{len(produites)} pages écrites, plus favicon.svg et le bouton mobile.")


if __name__ == "__main__":
    main()
