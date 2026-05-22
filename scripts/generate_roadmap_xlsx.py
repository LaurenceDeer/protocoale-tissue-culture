"""Generează ROADMAP-HUB.xlsx — checklist static pentru evoluția site-ului."""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ROADMAP-HUB.xlsx"

HEADER_FILL = PatternFill("solid", fgColor="1A1A1A")
HEADER_FONT = Font(bold=True, color="FFB000", size=11)
DONE_COL = "A"
COLS = ["Bifat", "ID", "Fază", "Săptămână", "Prioritate", "Task", "Notițe", "Data finalizare"]


def style_header(ws, row=1):
    for col, title in enumerate(COLS, 1):
        cell = ws.cell(row=row, column=col, value=title)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.freeze_panes = "A2"
    ws.row_dimensions[row].height = 28


def add_validation(ws, max_row):
    dv = DataValidation(
        type="list",
        formula1='"Da,Nu,În curs,Blocat,N/A"',
        allow_blank=True,
    )
    dv.error = "Alege: Da, Nu, În curs, Blocat sau N/A"
    dv.errorTitle = "Status bifat"
    ws.add_data_validation(dv)
    dv.add(f"{DONE_COL}2:{DONE_COL}{max_row}")


def set_widths(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


def add_rows(ws, rows, start=2):
    for r, row in enumerate(rows, start):
        for c, val in enumerate(row, 1):
            cell = ws.cell(row=r, column=c, value=val)
            if c == 6:
                cell.alignment = Alignment(wrap_text=True, vertical="top")
    return start + len(rows) - 1


def sheet_faze(wb):
    ws = wb.active
    ws.title = "1. Faze & Taskuri"
    style_header(ws)
    rows = [
        # Faza 0
        ("", "0.1", "0 — Fundație", "1", "Critic", "Repară linkurile din surse/Aprovizionare.md", "URL reale sau șterge rândul", ""),
        ("", "0.2", "0 — Fundație", "1", "Critic", "Creează pagina start-aici.md (traseu 30–60 min)", "Avertisment → Absolute Zero → Medii → Calculator → Drosera", ""),
        ("", "0.3", "0 — Fundație", "1", "Critic", "Banner status site (README + eventual sidebar)", "Ex: protocoale literatură, testare personală în curs", ""),
        ("", "0.4", "0 — Fundație", "1", "Medie", "Înlocuiește titlul WORK IN PROGRESS din Ghiduri.md", "Mesaj: hub activ, extindere graduală", ""),
        ("", "0.5", "0 — Fundație", "1", "Critic", "Publică ROADMAP.md pe site (versiune web a planului)", "Link din footer sau Start aici", ""),
        ("", "0.6", "0 — Fundație", "1", "Mică", "Adaugă robots.txt + verifică sitemap", "Allow: / + URL sitemap GitHub Pages", ""),
        # Faza 1
        ("", "1.1", "1 — Structură hub", "2", "Critic", "Standard metadata protocoale (YAML front matter)", "status, hormoni, ultima_actualizare, versiune", ""),
        ("", "1.2", "1 — Structură hub", "2", "Critic", "Badge-uri în _layouts/protocol.html", "dificultate, categorie, status, dată", ""),
        ("", "1.3", "1 — Structură hub", "2", "Medie", "CHANGELOG.md sau pagină status.md", "Update manual la fiecare release", ""),
        ("", "1.4", "1 — Structură hub", "3", "Critic", "Index protocoale filtrabil (Protocoale.md)", "după categorie, dificultate, hormoni", ""),
        ("", "1.5", "1 — Structură hub", "3", "Mare", "ghiduri/checklist-laborator.md (print-friendly)", "checkbox-uri pentru laborator", ""),
        ("", "1.6", "1 — Structură hub", "3", "Medie", "Fix glossary: ppm (unitate) vs PPM (biocid PCT)", "două intrări separate în glossary.js", ""),
        ("", "1.7", "1 — Structură hub", "2", "Medie", "Card Philodendron WIP → link ROADMAP", "nu card mort fără acțiune", ""),
        # Faza 2
        ("", "2.1", "2 — Conținut fără lab", "4", "Mare", "Protocol nou: Saintpaulia (status: literatura)", "Tier 1 roadmap specii", ""),
        ("", "2.2", "2 — Conținut fără lab", "5", "Medie", "Diagrame Mermaid în Troubleshooting", "flux contaminare / decizie", ""),
        ("", "2.3", "2 — Conținut fără lab", "4", "Medie", "Ilustrații stock CC0 (mucegai vs bacterii)", "Wikimedia, cu credit", ""),
        ("", "2.4", "2 — Conținut fără lab", "5", "Mare", "Șablon protocol în CONTRIBUTING.md", "secțiuni + metadata obligatorii", ""),
        ("", "2.5", "2 — Conținut fără lab", "5", "Medie", "GitHub Issue templates", "protocol nou, corectare, hall of fame", ""),
        ("", "2.6", "2 — Conținut fără lab", "6", "Medie", "Căutare îmbunătățită (Pagefind sau search.json cu content)", "când ai 8+ pagini", ""),
        ("", "2.7", "2 — Conținut fără lab", "6", "Mare", "Protocol nou: Musa/bananier (literatura)", "Tier 1", ""),
        ("", "2.8", "2 — Conținut fără lab", "6", "Mare", "Protocol nou: Nepenthes (literatura)", "Tier 1", ""),
        # Faza 3
        ("", "3.1", "3 — Cu echipament", "—", "Blocat echipament", "Achiziție echipament minim (SAB, oală, MS, cântar)", "vezi Aprovizionare + Notion", ""),
        ("", "3.2", "3 — Cu echipament", "—", "Blocat echipament", "Primele poze reale în protocoale testate", "înlocuiește placeholder doar unde ai rulat", ""),
        ("", "3.3", "3 — Cu echipament", "—", "Blocat echipament", "Actualizare status: in-testare → validat-ro", "notă: X/Y borcane curate, dată", ""),
        ("", "3.4", "3 — Cu echipament", "—", "Blocat echipament", "Deschide Hall of Fame pentru contribuții", "după primele reușite", ""),
        ("", "3.5", "3 — Cu echipament", "—", "Blocat echipament", "FAQ din întrebări reale (Issues/Giscus/mail)", "nu înainte de audiență", ""),
        ("", "3.6", "3 — Cu echipament", "—", "Opțional", "Video scurt setup SAB (YouTube embed)", "", ""),
        # Faza 4
        ("", "4.1", "4 — Distribuție", "8", "Mare", "Post comunitate RO (FB/Discord plante)", "link Start aici, nu spam", ""),
        ("", "4.2", "4 — Distribuție", "8", "Medie", "Thread Reddit relevant (EN)", "RO open TC guide", ""),
        ("", "4.3", "4 — Distribuție", "8", "Medie", "Cerere feedback structurat", "„Ai găsit Drosera în <5 min?”", ""),
        ("", "4.4", "4 — Distribuție", "8", "Critic", "Lansare Hub v1.0 (mesaj public)", "nu mai „WIP” — „literatură + validare în curs”", ""),
        # Definition of done
        ("", "DOD.1", "Definition of Done v1.0", "—", "Critic", "✓ Start aici există și e linkat de pe homepage", "", ""),
        ("", "DOD.2", "Definition of Done v1.0", "—", "Critic", "✓ Metadata + badge pe toate protocoalele", "", ""),
        ("", "DOD.3", "Definition of Done v1.0", "—", "Critic", "✓ Index filtrabil funcțional", "", ""),
        ("", "DOD.4", "Definition of Done v1.0", "—", "Critic", "✓ 0 linkuri moarte în tabele Aprovizionare", "", ""),
        ("", "DOD.5", "Definition of Done v1.0", "—", "Critic", "✓ ROADMAP public + checklist print", "", ""),
        ("", "DOD.6", "Definition of Done v1.0", "—", "Critic", "✓ Status literatura vs validat vizibil pe site", "", ""),
    ]
    last = add_rows(ws, rows)
    add_validation(ws, last)
    set_widths(ws, [10, 8, 18, 10, 12, 52, 36, 14])


def sheet_calendar(wb):
    ws = wb.create_sheet("2. Calendar 8 săpt")
    style_header(ws)
    rows = [
        ("", "S1", "Calendar", "1", "—", "Linkuri + start-aici + banner + ROADMAP.md + robots.txt", "", ""),
        ("", "S2", "Calendar", "2", "—", "Metadata + badge layout + CHANGELOG", "", ""),
        ("", "S3", "Calendar", "3", "—", "Index filtrabil + checklist print + glossary fix", "", ""),
        ("", "S4", "Calendar", "4", "—", "1 protocol nou + diagrame Troubleshooting", "", ""),
        ("", "S5", "Calendar", "5", "—", "Issue templates + șablon CONTRIBUTING", "", ""),
        ("", "S6", "Calendar", "6", "—", "1 protocol nou + search îmbunătățit", "", ""),
        ("", "S7", "Calendar", "7", "—", "feed.xml + status.md + polish SEO descriptions", "", ""),
        ("", "S8", "Calendar", "8", "—", "Lansare v1.0 + post comunitate + feedback", "", ""),
    ]
    last = add_rows(ws, rows)
    add_validation(ws, last)
    set_widths(ws, [10, 8, 18, 10, 12, 52, 36, 14])


def sheet_specii(wb):
    ws = wb.create_sheet("3. Specii (protocoale)")
    style_header(ws)
    rows = [
        ("", "P-01", "Live", "—", "—", "Drosera spatulata", "există", ""),
        ("", "P-02", "Live", "—", "—", "Monstera deliciosa / Thai", "există", ""),
        ("", "P-03", "Live", "—", "—", "Thuja occidentalis", "există", ""),
        ("", "P-04", "Live", "—", "—", "Phalaenopsis", "există", ""),
        ("", "P-05", "Tier 1", "4–6", "Mare", "Saintpaulia (violetă africană)", "literatura, începători", ""),
        ("", "P-06", "Tier 1", "6", "Mare", "Musa / bananier", "literatura", ""),
        ("", "P-07", "Tier 1", "6", "Mare", "Nepenthes", "carnivore, audiență existentă", ""),
        ("", "P-08", "Tier 2", "—", "Medie", "Philodendron Pink Princess", "WIP — finalizează 2+ surse", ""),
        ("", "P-09", "Tier 2", "—", "Medie", "Anthurium", "aroide, fenolizare", ""),
        ("", "P-10", "Tier 2", "—", "Medie", "Hoya", "noduri, cerere RO", ""),
        ("", "P-11", "Tier 2", "—", "Medie", "Capsicum (ardei) — din semințe", "flux diferit de vegetativ", ""),
        ("", "P-12", "Tier 3", "—", "Mică", "Alocasia", "mai târziu", ""),
        ("", "P-13", "Tier 3", "—", "Mică", "Ficus", "mai târziu", ""),
        ("", "P-14", "Tier 3", "—", "Mică", "Germinare semințe orchid avansat", "mai târziu", ""),
        ("", "P-15", "Tier 3", "—", "Opțional", "Cannabis TC", "secțiune separată + disclaimer legal sau skip", ""),
    ]
    last = add_rows(ws, rows)
    add_validation(ws, last)
    set_widths(ws, [10, 8, 18, 10, 12, 52, 36, 14])


def sheet_amanate(wb):
    ws = wb.create_sheet("4. Amânate & Viitor")
    style_header(ws)
    rows = [
        ("", "A-01", "Amânat", "—", "Blocat echipament", "Poze proprii în protocoale", "după primul experiment", ""),
        ("", "A-02", "Amânat", "—", "Blocat audiență", "Hall of Fame populat", "după ~50–100 vizitatori/lună sau contribuții", ""),
        ("", "A-03", "Amânat", "—", "Blocat audiență", "FAQ central", "extrage din întrebări reale", ""),
        ("", "A-04", "Amânat", "—", "Mică", "RSS/Atom feed (feed.xml)", "15 min Jekyll; după Start aici", ""),
        ("", "A-05", "Amânat", "—", "Mică", "Giscus pe ghiduri (nu doar protocoale)", "când ai trafic pe ghiduri", ""),
        ("", "A-06", "Amânat", "—", "Medie", "All Contributors badge în README", "după primele PR-uri externe", ""),
        ("", "A-07", "Amânat", "—", "Medie", "schema.org HowTo + Open Graph imagini", "SEO avansat", ""),
        ("", "A-08", "Amânat", "—", "Medie", "YAML/JSON rețete partajate cu calculatorul", "sursă unică de adevăr", ""),
        ("", "A-09", "Amânat", "—", "Medie", "GitHub Actions: htmlproofer / lychee link checker", "la fiecare PR", ""),
        ("", "A-10", "Amânat", "—", "Medie", "Netlify/Vercel preview pentru PR-uri", "review vizual", ""),
        ("", "A-11", "Amânat", "—", "Medie", "Extrage CSS din default.html în assets/css/site.css", "mentenanță", ""),
        ("", "A-12", "Amânat", "—", "Mică", "Pin versiuni CDN (nu @latest)", "simple-jekyll-search etc.", ""),
        ("", "A-13", "Amânat", "—", "Mică", "Fonturi self-hosted (fără Google Fonts)", "privacy + offline", ""),
        ("", "A-14", "Amânat", "—", "Evaluare", "MIGRARE: MkDocs Material", "când vrei search/tabs/versioning docs mai bogat; efort ~1–2 zile", ""),
        ("", "A-15", "Amânat", "—", "Evaluare", "MIGRARE: Astro + Starlight", "când vrei componente interactive complexe; efort ~3–5 zile", ""),
        ("", "A-16", "Amânat", "—", "Decizie", "Document decizie migrare (Jekyll vs MkDocs vs Astro)", "criterii: calculator, comentarii, tema, timp", ""),
        ("", "A-17", "Amânat", "—", "Opțional", "Lightbox imagini (GLightbox)", "când ai galerii reale", ""),
        ("", "A-18", "Amânat", "—", "Opțional", "Sci-Hub mutat în „resurse avansate” + disclaimer", "imagine proiect", ""),
        ("", "A-19", "Amânat", "—", "Opțional", "Licență CC BY-NC → discuție BY-SA pentru fork OS", "doar dacă vrei contribuții comerciale", ""),
    ]
    last = add_rows(ws, rows)
    add_validation(ws, last)
    set_widths(ws, [10, 8, 18, 10, 12, 52, 36, 14])


def sheet_legenda(wb):
    ws = wb.create_sheet("0. Cum folosești")
    ws["A1"] = "ROADMAP-HUB — Open Tissue Culture RO"
    ws["A1"].font = Font(bold=True, size=14, color="FFB000")
    lines = [
        "",
        "Actualizează acest fișier de fiecare dată când lucrezi la site.",
        "Coloana «Bifat»: Da | Nu | În curs | Blocat | N/A",
        "",
        "Status protocoale pe site (metadata):",
        "  • literatura — sinteză din articole, netestat personal",
        "  • in-testare — ai început experimente",
        "  • validat-ro — rulat de tine (sau contributor RO)",
        "  • comunitate — confirmat de altcineva cu dovezi",
        "",
        "Hub v1.0 = toate rândurile DOD.* bifate Da + lansare S8.",
        "",
        "Migrare MkDocs/Astro: vezi foaia «4. Amânate» — A-14 … A-16.",
        "Nu migra înainte de Hub v1.0 pe Jekyll (ai conținutul structurat mai întâi).",
        "",
        "Versiune document: 2026-05-19",
        "Repo: protocoale-tissue-culture",
    ]
    for i, line in enumerate(lines, 2):
        ws.cell(row=i, column=1, value=line)
    ws.column_dimensions["A"].width = 80


def main():
    wb = Workbook()
    sheet_legenda(wb)
    sheet_faze(wb)
    sheet_calendar(wb)
    sheet_specii(wb)
    sheet_amanate(wb)
    wb.save(OUT)
    print(f"Creat: {OUT}")


if __name__ == "__main__":
    main()
