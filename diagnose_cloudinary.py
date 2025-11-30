import os
import json
import cloudinary
from cloudinary.search import Search
from dotenv import load_dotenv

# Načtení klíčů
load_dotenv()

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)

def diagnose_file(filename):
    print(f"--- DIAGNOSTIKA SOUBORU: {filename} ---")
    
    # Hledáme konkrétní soubor podle jména (ignorujeme složky)
    try:
        result = Search()\
            .expression(f"filename:{filename}")\
            .max_results(1)\
            .execute()
        
        resources = result.get('resources', [])
        
        if not resources:
            print("❌ Soubor nenalezen! Zkontroluj, jestli jsi API klíče zkopíroval správně.")
            return

        # Vypíšeme, co jsme našli
        file_data = resources[0]
        print("✅ Soubor nalezen!")
        print(f"Public ID (skutečné jméno): {file_data.get('public_id')}")
        print(f"Folder (Složka v metadatech): {file_data.get('folder')}")
        print(f"Asset Folder (Nová složka): {file_data.get('asset_folder')}")
        
        print("\n--- KOMPLETNÍ DATA (pro kontrolu) ---")
        print(json.dumps(file_data, indent=2))

    except Exception as e:
        print(f"Chyba: {e}")

if __name__ == "__main__":
    # Název souboru přesně tak, jak je na screenshotu (bez přípony jpg/png)
    SOUBOR_NA_TEST = "Dolomity_9_it1wwd" 
    
    diagnose_file(SOUBOR_NA_TEST)
