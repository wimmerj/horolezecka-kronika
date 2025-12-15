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
    cloud_folder: Název složky NA CLOUDINARY (dle asset_folder)
    output_md_path: Kam uložit .md soubor na disku
    title: Nadpis na webu
    """
    
    print(f"--- Připojuji se k Cloudinary a hledám složku: '{cloud_folder}' ---")
    
    try:
        # Získání seznamu obrázků ve složce pomocí Search API
        result = Search()\
            .expression(f'asset_folder="{cloud_folder}"')\
            .sort_by('public_id', 'asc')\
            .max_results(500)\
            .execute()
        
        resources = result.get('resources', [])
        
        if not resources:
            print("CHYBA: Složka je prázdná nebo neexistuje!")
            return

        print(f"Nalezeno {len(resources)} fotek. Generuji Filmstrip galerii...")

        # --- PŘÍPRAVA OBSAHU ---

        # 1. Načtení existujícího obsahu souboru (pokud existuje)
        existing_content = ""
        if os.path.exists(output_md_path):
            with open(output_md_path, "r", encoding="utf-8") as f:
                existing_content = f.read()
            
            # --- LOGIKA PRO ODSTRANĚNÍ STARÉ GALERIE ---
            # Hledáme začátek galerie, abychom ji mohli nahradit novou verzí
            gallery_start = -1
            
            # Zkusíme najít nadpis
            p_gallery = existing_content.find('## :camera: Fotogalerie')
            
            if p_gallery != -1:
                gallery_start = p_gallery
            else:
                # Fallback: Zkusíme najít začátek divu (starý grid nebo nový scroll)
                p_grid = existing_content.find('<div class="grid cards" markdown>')
                p_scroll = existing_content.find('<div class="gallery-scroll" markdown>')
                
                if p_grid != -1:
                    gallery_start = p_grid
                elif p_scroll != -1:
                    gallery_start = p_scroll
            
            # Pokud jsme našli začátek galerie, ořízneme obsah před ní
            if gallery_start != -1:
                existing_content = existing_content[:gallery_start].rstrip()
        
        # 2. Sestavení finálního obsahu
        final_content = existing_content
        
        # Přidání odřádkování, pokud soubor nekončí prázdným řádkem
        if existing_content and not existing_content.endswith('\n\n'):
            final_content += "\n\n"
        
        final_content += "---\n\n"
        final_content += "## :camera: Fotogalerie\n\n"
        
        # ZMĚNA: Používáme div BEZ markdown atributu a čistý HTML
        final_content += '<div class="gallery-scroll">\n'
        
        for res in resources:
            url = res['secure_url']
            filename = res['public_id'].split('/')[-1] # Získáme název souboru
            
            # A) THUMBNAIL (Náhled v pásu) - menší výška pro filmstrip
            thumb_url = url.replace('/upload/', '/upload/f_auto,q_auto,h_200,c_fill/')
            
            # B) LIGHTBOX (Velký náhled po kliknutí)
            lightbox_url = url.replace('/upload/', '/upload/f_auto,q_auto,w_1920/')

            # C) ORIGINÁL (Pro stažení)
            original_url = url

            # D) POPISEK - HTML entitami escapovaný
            description_html = (
                f"Fotografie: {filename} &lt;br&gt; "
                f"&lt;a href='{original_url}' target='_blank' style='color: #4051b5; font-weight: bold; text-decoration: none;'&gt;"
                f"⬇️ Stáhnout plnou kvalitu&lt;/a&gt;"
            )

            # E) ČISTÝ HTML řádek (GLightbox pracuje s HTML, ne s markdown)
            line = f'<a href="{lightbox_url}" data-gallery="gallery" data-description="{description_html}"><img src="{thumb_url}" alt="{filename}"></a>\n'
            
            final_content += line
        
        final_content += "</div>\n"
        
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
    print("=== Generování galerií (Filmstrip Mode) ===\n")
    for gallery in galleries:
        generate_md_from_cloud(
            gallery["cloud_folder"],
            gallery["output_path"],
            gallery["title"]
        )
        print()
    
    print("=== Všechny galerie byly vygenerovány ===")