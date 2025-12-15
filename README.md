# Horolezecká Kronika - MkDocs Web

Webové stránky pro kroniku horolezeckých výprav vytvořené pomocí MkDocs s Material theme.

## 📋 Struktura projektu

```
horolezecka-kronika/
├── mkdocs.yml              # Konfigurace MkDocs
├── docs/
│   ├── index.md           # Úvodní stránka
│   ├── o-nas.md           # O našem týmu
│   ├── planovana-dovolena-2026.md
│   ├── 2025-slovinsko.md
│   ├── 2024-italie-ledro-2.md
│   ├── 2023-italie-ledro-1.md
│   ├── 2022-dolomity-2.md
│   ├── 2021-dolomity-1.md
│   ├── images/            # Složka pro obrázky
│   │   ├── uvod-hero.jpg
│   │   ├── 2026/
│   │   ├── 2025/
│   │   ├── 2024/
│   │   ├── 2023/
│   │   ├── 2022/
│   │   ├── 2021/
│   │   └── team/
│   └── stylesheets/
│       └── extra.css      # Vlastní CSS styly
└── README.md
```

## 🚀 Jak začít

### 1. Instalace MkDocs a pluginů

```powershell
pip install mkdocs
pip install mkdocs-material
pip install mkdocs-glightbox
```

### 2. Spuštění lokálního serveru

```powershell
mkdocs serve
```

Stránky budou dostupné na: `http://127.0.0.1:8000`

### 3. Build pro produkci

```powershell
mkdocs build
```

## 📸 Přidání fotografií

1. Vytvořte podsložku v `docs/images/` pro každý rok (např. `2026/`)
2. Nahrajte fotografie do příslušné složky
3. V Markdown souborech používejte relativní cesty:

```markdown
![Popis](images/2026/moje-fotka.jpg){ width="600" }
```

### Doporučené rozměry obrázků

- **Header obrázky**: 1920 x 600 px
- **Fotogalerie**: 1200 x 800 px
- **Thumbnaily**: 400 x 300 px
- **Profilové fotky týmu**: 600 x 600 px

## 🎬 Vkládání YouTube videí

```markdown
<iframe width="100%" height="450" 
  src="https://www.youtube.com/embed/VIDEO_ID" 
  frameborder="0" allowfullscreen>
</iframe>
```

Nahraďte `VIDEO_ID` skutečným ID vašeho videa z YouTube URL.

## 🗺️ Vkládání Google Maps

```markdown
<iframe 
  src="https://www.google.com/maps/embed?pb=EMBED_CODE" 
  width="100%" height="450" 
  style="border:0;" allowfullscreen>
</iframe>
```

Pro získání embed kódu:
1. Otevřete Google Maps
2. Klikněte na "Sdílet"
3. Vyberte "Vložit mapu"
4. Zkopírujte kód

## 🔗 Odkazy na galerie

### Google Drive
1. Nahrajte fotografie do Google Drive
2. Sdílejte složku s nastaveným "Kdokoli s odkazem může zobrazit"
3. Zkopírujte odkaz do stránky

### OneDrive
1. Nahrajte fotografie do OneDrive
2. Klikněte na "Sdílet"
3. Vygenerujte odkaz pro zobrazení
4. Vložte do stránky

## ⚙️ Konfigurace

### Změna barev tématu

V `mkdocs.yml` upravte sekci `theme.palette`:

```yaml
palette:
  primary: blue grey  # Hlavní barva
  accent: deep orange # Zvýrazňovací barva
```

### Přidání nové stránky

1. Vytvořte nový `.md` soubor v `docs/`
2. Přidejte ho do navigace v `mkdocs.yml`:

```yaml
nav:
  - Název stránky: soubor.md
```

## 📝 Markdown tipy

### Obrázky vedle sebe

```markdown
<div class="image-grid">
![](images/foto1.jpg){ width="48%" }
![](images/foto2.jpg){ width="48%" }
</div>
```

### Informační boxy

```markdown
!!! info "Nadpis"
    Text informace

!!! warning "Varování"
    Text varování

!!! tip "Tip"
    Text tipu

!!! success "Úspěch"
    Text úspěchu
```

### Topografie výstupů

```markdown
```
START: Místo (výška)
├── Část 1
├── Část 2
└── CÍL: Vrchol
```‌```

## 🌐 Publikování

### GitHub Pages

1. Vytvořte GitHub repository
2. Push kód do repozitáře
3. Spusťte:

```powershell
mkdocs gh-deploy
```

Stránky budou dostupné na: `https://username.github.io/repository/`

## 📱 Responzivní design

Stránky jsou plně responzivní díky Material theme. Automaticky se přizpůsobí:
- 📱 Mobilním telefonům
- 📱 Tabletům
- 💻 Desktopům

## 🎨 Vlastní styly

Vlastní CSS jsou v `docs/stylesheets/extra.css`. Můžete je upravit podle potřeby.

## 🔍 Vyhledávání

Vyhledávání je aktivní automaticky. Podporuje češtinu díky nastavení:

```yaml
plugins:
  - search:
      lang: cs
```

## 📦 Potřebné balíčky

- Python 3.7+
- mkdocs
- mkdocs-material
- mkdocs-glightbox (pro lightbox fotogalerií)

## 💡 Tipy pro použití

1. **Pravidelně zálohujte fotografie** - používejte cloud úložiště
2. **Optimalizujte obrázky** před nahráním (snižte velikost)
3. **Používejte popisné názvy souborů** (např. `2025-triglav-vrchol.jpg`)
4. **Testujte na různých zařízeních** před publikováním
5. **Pravidelně aktualizujte** po každé výpravě

## 🆘 Časté problémy

### MkDocs serve nefunguje
- Zkontrolujte, zda máte nainstalované všechny balíčky
- Ověřte, že jste ve správné složce

### Obrázky se nezobrazují
- Zkontrolujte cesty k obrázkům (case-sensitive!)
- Ověřte, že jsou obrázky ve správné složce

### Změny se neprojevují
- Hard refresh v prohlížeči (Ctrl+F5)
- Restartujte `mkdocs serve`

## 📞 Kontakt

Pro otázky a návrhy kontaktujte: info@horolezci.cz

---

**Vytvořeno s ❤️ pro horolezce a dobrodruhy**
