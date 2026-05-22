---
layout: default
title: Roadmap & Plan de Dezvoltare
description: "Fazele de dezvoltare ale hub-ului Open Tissue Culture RO. Vezi progresul curent și planurile de viitor."
---

# 🗺️ Roadmap & Plan de Dezvoltare

Acesta este planul public de dezvoltare pentru hub-ul **Open Tissue Culture RO**. Actualizăm acest document pe măsură ce avansăm cu implementările și validările în laborator.

---

## 🏁 Faza 0: Fundație (Săptămâna 1) — 🟢 Finalizată

Faza de pregătire a infrastructurii de bază a site-ului.

*   `[x]` **0.1** Repară linkurile din [Aprovizionare.md](./surse/Aprovizionare.html) cu legături directe către furnizori reali din România.
*   `[x]` **0.2** Creează pagina [Start Aici](./start-aici.html) (traseul de învățare rapidă de 30-60 de minute).
*   `[x]` **0.3** Banner cu statusul curent al site-ului (în README și sidebar).
*   `[x]` **0.4** Înlocuiește mesajul temporar "WORK IN PROGRESS" din [Ghiduri.html](./Ghiduri.html).
*   `[x]` **0.5** Publică documentul `ROADMAP.md` pe website.
*   `[x]` **0.6** Adaugă `robots.txt` și configurează sitemap-ul pentru o mai bună indexare în motoarele de căutare.

---

## 🏗️ Faza 1: Structură hub (Săptămânile 2-3) — 🟡 În Curs

Organizarea conținutului existent și pregătirea elementelor tehnice.

*   `[ ]` **1.1** Standardizare metadate pentru protocoale (YAML front matter: status, dificultate, hormoni utilizați, ultima actualizare).
*   `[ ]` **1.2** Badge-uri dinamice în layout-ul de protocol (`_layouts/protocol.html`) pentru a vizualiza ușor statusul.
*   `[ ]` **1.3** Adăugare pagină de `status.md` / `CHANGELOG.md` pentru a urmări actualizările istorice.
*   `[ ]` **1.4** Index protocoale complet filtrabil și sortabil pe pagina [Protocoale](./protocoale/Protocoale.html).
*   `[ ]` **1.5** Creare `ghiduri/checklist-laborator.md` — fișă gata de imprimat (print-friendly) pentru activitatea sterilă în SAB.
*   `[ ]` **1.6** Corectare dicționar/glosar: definirea diferenței dintre `ppm` (părți per milion, unitate de măsură) și `PPM` (Plant Preservative Mixture, biocid) în `glossary.js`.
*   `[ ]` **1.7** Actualizare card Philodendron (în lucru) cu link direct către această pagină de Roadmap.

---

## 📝 Faza 2: Conținut de Literatură (Săptămânile 4-6) — 🔴 Neîncepută

Extinderea ghidurilor teoretice și a rețetelor bazate pe articole științifice.

*   `[ ]` **2.1** Protocol nou bazat pe literatură: *Saintpaulia* (violeta africană) — specie perfectă pentru începători.
*   `[ ]` **2.2** Diagrame Mermaid explicative în ghidul de [Troubleshooting](./ghiduri/Troubleshooting.html) pentru diagnosticarea rapidă a contaminărilor.
*   `[ ]` **2.3** Adăugare ilustrații și imagini stock libere de drepturi (mucegaiuri, bacterii, explante necrozate).
*   `[ ]` **2.4** Creare șablon de protocol standardizat în `CONTRIBUTING.md` pentru a facilita contribuțiile externe.
*   `[ ]` **2.5** Template-uri GitHub pentru raportarea problemelor sau propunerea de protocoale noi.
*   `[ ]` **2.6** Îmbunătățirea motorului de căutare intern (Pagefind sau indexare completă în `search.json`).
*   `[ ]` **2.7** Protocol nou: *Musa* (Bananier).
*   `[ ]` **2.8** Protocol nou: *Nepenthes* (Plantă carnivoră).

---

## 🔬 Faza 3: Cu Echipament (Blocată temporar) — 🔒 În așteptare

Trecerea la validarea practică. Necesită achiziția și calibrarea echipamentelor.

*   `[ ]` **3.1** Achiziție echipament de laborator minim (SAB stabil, oală sub presiune dedicată, substanțe MS, cântar fin).
*   `[ ]` **3.2** Înlocuirea pozelor stock/placeholders cu poze reale din propriul laborator.
*   `[ ]` **3.3** Actualizarea statusului protocoalelor testate din `in-testare` în `validat-ro`.
*   `[ ]` **3.4** Deschiderea oficială a secțiunii *Hall of Fame* pentru cultivatorii români care aduc dovezi de succes.
*   `[ ]` **3.5** Creare secțiune de Întrebări Frecvente (FAQ) extrase din interacțiunile reale cu comunitatea.
*   `[ ]` **3.6** Ghid video scurt sau ilustrat pas-cu-pas pentru asamblarea și dezinfectarea unui SAB pliabil.

---

## 📢 Faza 4: Distribuție & Lansare — 🔴 Neîncepută

*   `[ ]` **4.1** Postări informative pe comunitățile românești de profil (Grupuri de Facebook de plante, Discord-uri de botanică).
*   `[ ]` **4.2** Prezentare pe comunitățile internaționale (Reddit r/tissueculture etc.).
*   `[ ]` **4.3** Implementare sistem de feedback rapid pentru cititori.
*   `[ ]` **4.4** **Lansare oficială Hub v1.0** (eliminarea tag-urilor WIP pe zonele de bază).

---

## 🎯 Definition of Done (DOD) v1.0

Hub-ul este considerat complet pentru versiunea 1.0 când:
1. Pagina **Start Aici** este completă și este vizibilă pe prima pagină.
2. Toate protocoalele au metadate standardizate și badge-uri de status funcționale.
3. Indexul de protocoale poate fi filtrat cu succes.
4. Pagina de **Aprovizionare** are exclusiv linkuri funcționale de pe piața internă.
5. Există o pagină web publică pentru **Roadmap**.
6. Diferența dintre protocoalele testate practic (`validat-ro`) și cele din cărți (`literatura`) este marcată vizibil la fiecare pas.
