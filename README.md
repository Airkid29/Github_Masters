# Documentation du Script `scraper.py`

## Description

Le script `scraper.py` est un outil conçu pour effectuer le scraping de fichiers HTML locaux. Il utilise la bibliothèque `BeautifulSoup` pour analyser le contenu des fichiers HTML et extraire des informations spécifiques telles que les titres, les sections, les images, les paragraphes et les liens.

## Fonctionnalités

Voici les principales fonctionnalités du script :

1. **Extraction du titre de la page** :
   - Le script récupère et affiche le titre de la page HTML si celui-ci est défini.

2. **Extraction du titre principal (balise `<h1>`)** :
   - Si une balise `<h1>` est présente, son contenu est affiché.

3. **Analyse des sections** :
   - Le script identifie les balises `<section>` et affiche les titres des sous-sections (balises `<h2>`).

4. **Liste des images** :
   - Toutes les balises `<img>` sont analysées, et leurs attributs `src` sont affichés.

5. **Extraction des paragraphes** :
   - Le contenu de toutes les balises `<p>` est affiché.

6. **Liste des liens** :
   - Le script identifie toutes les balises `<a>` et affiche leurs attributs.

## Structure du Code

- **Importation des bibliothèques** :
  - Le script utilise la bibliothèque `BeautifulSoup` pour le parsing HTML.

- **Fonction principale `scrape_page(filename)`** :
  - Cette fonction prend en entrée le nom d'un fichier HTML et effectue les opérations de scraping décrites ci-dessus.
  - Gestion des erreurs :
    - Si le fichier n'est pas trouvé, un message d'erreur est affiché.
    - Les autres exceptions sont également capturées et affichées.

- **Bloc principal (`__main__`)** :
  - Le script exécute le scraping sur deux fichiers HTML : `index.html` et `apropos.html`.

## Prérequis

- Python 3.x
- Bibliothèque `BeautifulSoup` (incluse dans le package `bs4`)

Pour installer la bibliothèque requise, exécutez la commande suivante :
```bash
pip install beautifulsoup4
```

## Utilisation

1. Placez les fichiers HTML à analyser dans le même répertoire que le script `scraper.py`.
2. Exécutez le script avec la commande suivante :
```bash
python scraper.py
```
3. Les résultats du scraping seront affichés dans la console.

## Exemple de Résultat

Pour un fichier `index.html` contenant :
```html
<html>
<head>
    <title>Exemple</title>
</head>
<body>
    <h1>Bienvenue</h1>
    <section>
        <h2>Introduction</h2>
    </section>
    <img src="image1.jpg" />
    <p>Ceci est un paragraphe.</p>
    <a href="https://example.com">Lien</a>
</body>
</html>
```
Le script affichera :
```
--- Scraping index.html ---

Titre de la page : Exemple
Titre principal (h1) : Bienvenue

Nombre de sections trouvées : 1
 - Section : Introduction

Nombre d'images trouvées : 1
 - Image : image1.jpg

les paragraphes presents sur ce site:
Ceci est un paragraphe.

Nombre de liens trouvés : 1
 - Liens : https://example.com
```

## Auteur
Ce script a été développé pour des besoins éducatifs et de démonstration.

## Limitations
- Le script ne gère que les fichiers HTML locaux.
- Certaines fonctionnalités (comme l'extraction des vidéos) sont commentées et non implémentées.

## Améliorations Futures
- Ajouter la prise en charge des fichiers HTML distants via des requêtes HTTP.
- Implémenter l'extraction des vidéos.
- Générer un rapport de scraping sous forme de fichier texte ou JSON.