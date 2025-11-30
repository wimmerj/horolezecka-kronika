import os
import cloudinary
import cloudinary.api
from cloudinary.search import Search
from dotenv import load_dotenv

# 1. Načtení API klíčů
load_dotenv()

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)

def generate_md_from_cloud(cloud_folder, output_md_path, title):
    """
    cloud_folder: Název složky NA CLOUDINARY (např. "alpy_2024")
    output_md_path: Kam uložit .md soubor na disku
    title: Nadpis na webu
    """
    
    print(f"--- Připojuji se k Cloudinary a hledám složku: '{cloud_folder}' ---")
    
    try:
        # Získání seznamu obrázků ve složce pomocí Search API
        # Hledáme podle asset_folder (Media Library složka)
        result = Search()\
            .expression(f'asset_folder="{cloud_folder}"')\
            .sort_by('public_id', 'asc')\
            .max_results(500)\
            .execute()
        
        resources = result.get('resources', [])
        
        if not resources:
            print("CHYBA: Složka je prázdná nebo neexistuje!")
            return

        print(f"Nalezeno {len(resources)} fotek. Generuji Markdown...")



        # Přidání galerie na konec existujícího souboru
        # Nejprve zkontrolujeme, jestli soubor existuje
        existing_content = ""
        if os.path.exists(output_md_path):
            with open(output_md_path, "r", encoding="utf-8") as f:
                existing_content = f.read()
            
            # Pokud už v souboru galerie existuje, odebereme ji
            if '<div class="grid cards" markdown>' in existing_content:
                # Najdeme začátek galerie
                gallery_start = existing_content.find('## :camera: Fotogalerie')
                if gallery_start == -1:
                    gallery_start = existing_content.find('<div class="grid cards" markdown>')
                
                if gallery_start != -1:
                    existing_content = existing_content[:gallery_start].rstrip()
        
        # Vytvoření kompletního obsahu s galerií
        final_content = existing_content
        if existing_content and not existing_content.endswith('\n\n'):
            final_content += "\n\n"
        
        final_content += "---\n\n"
        final_content += "## :camera: Fotogalerie\n\n"
        final_content += '<div class="grid cards" markdown>\n\n'
        
        # Už jsou seřazené díky sort_by v Search API
        for res in resources:
            url = res['secure_url']
            filename = res['public_id'].split('/')[-1] # Získáme název souboru pro alt text
            
            # Cloudinary triky pro optimalizaci:
            # Thumbnail (náhled): šířka 600px, kvalita auto
            thumb_url = url.replace('/upload/', '/upload/f_auto,q_auto,w_600/')
            
            # Full size (po kliknutí): jen optimalizace komprese, plná velikost
            full_url = url.replace('/upload/', '/upload/f_auto,q_auto/')

            # Přidání řádku do galerie
            final_content += f"-   [![{filename}]({thumb_url})]({full_url})\n"
        
        final_content += "\n</div>\n"
        
        # Uložení
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(final_content)

        print(f"--- HOTOVO! Soubor uložen zde: {output_md_path} ---")

    except Exception as e:
        print(f"Došlo k chybě: {e}")

# --- NASTAVENÍ ---
if __name__ == "__main__":
    
    # Definice všech galerií
    galleries = [
        {
            "cloud_folder": "2021-dolomity-1",
            "output_path": r"docs\2021-dolomity-1.md",
            "title": "Dolomity 2021 - První expedice"
        },
        {
            "cloud_folder": "2022-dolomity-2",
            "output_path": r"docs\2022-dolomity-2.md",
            "title": "Dolomity 2022 - Druhá expedice"
        },
        {
            "cloud_folder": "2023-italie-ledro-1",
            "output_path": r"docs\2023-italie-ledro-1.md",
            "title": "Itálie - Lago di Ledro 2023"
        },
        {
            "cloud_folder": "2024-italie-ledro-2",
            "output_path": r"docs\2024-italie-ledro-2.md",
            "title": "Itálie - Lago di Ledro 2024"
        },
        {
            "cloud_folder": "2025-slovinsko",
            "output_path": r"docs\2025-slovinsko.md",
            "title": "Slovinsko 2025"
        }
    ]
    
    # Vygenerování všech galerií
    print("=== Generování galerií ===\n")
    for gallery in galleries:
        generate_md_from_cloud(
            gallery["cloud_folder"],
            gallery["output_path"],
            gallery["title"]
        )
        print()  # Prázdný řádek mezi galeriemi
    
    print("=== Všechny galerie byly vygenerovány ===")
    
