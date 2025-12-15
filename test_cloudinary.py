import os
import cloudinary
import cloudinary.api
from dotenv import load_dotenv

# Načtení API klíčů
load_dotenv()

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)

print("=== TEST CLOUDINARY API ===\n")

# 1. Test připojení
print("1. Testování připojení...")
print(f"   Cloud Name: {os.getenv('CLOUDINARY_CLOUD_NAME')}")
print(f"   API Key: {os.getenv('CLOUDINARY_API_KEY')[:10]}...")
print()

# 2. Získání seznamu všech souborů
try:
    print("2. Získávám seznam všech souborů...")
    result = cloudinary.api.resources(
        type="upload",
        max_results=500
    )
    
    resources = result.get('resources', [])
    print(f"   Celkem nalezeno: {len(resources)} souborů\n")
    
    # 3. Vypsat všechny unikátní složky
    print("3. Nalezené složky (z public_id cest):")
    folders = set()
    for res in resources:
        public_id = res['public_id']
        if '/' in public_id:
            folder = public_id.rsplit('/', 1)[0]
            folders.add(folder)
    
    if folders:
        for folder in sorted(folders):
            print(f"   - {folder}")
    else:
        print("   Žádné složky nenalezeny (soubory jsou v rootu)")
    
    print()
    
    # 4. Ukázka prvních 5 souborů
    print("4. Ukázka prvních 5 souborů:")
    for i, res in enumerate(resources[:5], 1):
        print(f"   {i}. {res['public_id']}")
        print(f"      URL: {res['secure_url']}")
        print()

except Exception as e:
    print(f"CHYBA: {e}")
    print("\nMožné příčiny:")
    print("- Špatné API klíče")
    print("- Chybí přístupová práva")
    print("- Problém se sítí")
