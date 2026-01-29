#Importation des bibliothèques
from bs4 import BeautifulSoup

print("--------------BILAN FINAL DU SCRAPING---------------")

print("\n")
def scrape_page(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            
        print(f"--- Scraping {filename} ---")
        print("\n")
        
        # 1. Titre de la page
        if soup.title:
            print(f"Titre de la page : {soup.title.text}")
            
        # 2. H1 (Titre principal)
        h1 = soup.find("h1")
        if h1:
            print(f"Titre principal (h1) : {h1.text.strip()}")

            print("\n")
            
        # 3. Sections (h2 et contenu)
        sections = soup.find_all("section")
        if sections:
            print(f"\nNombre de sections trouvées : {len(sections)}")
            for section in sections:
                h2 = section.find("h2")
                if h2:
                    print(f" - Section : {h2.text.strip()}")

                print("\n")
                    
        # 4. Images
        images = soup.find_all("img")
        if images:
            print(f"\nNombre d'images trouvées : {len(images)}")
            for img in images:
                src = img.get("src")
                print(f" - Image : {src}")
                print("\n")
        
        '''# 5. Videos
        videos = soup.find_all("img")
        if images:
            print(f"\nNombre d'images trouvées : {len(images)}")
            for img in images:
                src = img.get("src")
                print(f" - Image : {src}")
                print("\n")'''

        # 5. Paragraphes (intro)
        print("les paragraphes presents sur ce site:")
        paragraphes = soup.find_all("p")
        for p in paragraphes:
            print("\n")
            print(p.text)

            print("\n")


        #6. Les liens du projet
        liens = soup.find_all("a")
        if liens: 
            print(f"\nNombre de liens trouvés :  {len(liens)}")
            for a in liens:
                src = img.get("a")
                print(f" - Liens : {a}")

                print("\n")

    except FileNotFoundError:
        print(f"Le fichier {filename} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    # On scrape la page index.html comme demandé
    scrape_page("index.html")

    print("\n")

    #Scraping de la page "APROPOS"
    scrape_page("apropos.html")

    print("\n")

