---
layout: default
title: Status Hub & Jurnal de Modificări
description: "Urmărește versiunea curentă a site-ului, ultimele actualizări și istoricul modificărilor aduse hub-ului."
---

# 📈 Status Hub & Jurnal de Modificări (Changelog)

Versiunea curentă a site-ului: **v0.1.2-beta**

Aici poți urmări evoluția hub-ului, modificările recente și istoricul lansărilor noastre.

---

## ⚡ Istoricul Versiunilor

### v0.1.2 — Filtrare & Instrumente de Lucru (Curentă)
*Data: 27 Mai 2026*

*   **Filtrare Interactivă Protocoale:** Implementarea unui sistem de filtre dinamice (Categorie, Dificultate, Hormoni) pe pagina de [Protocoale](./protocoale/Protocoale.html), folosind Javascript nativ pentru afișarea instantanee a speciilor.
*   **Fișă Checklist Laborator:** Crearea ghidului print-friendly [Checklist Laborator](./ghiduri/checklist-laborator.html) cu pași clari de verificare a sterilității și pregătirii mediilor, optimizat complet pentru tipărirea fizică la imprimantă.
*   **Corectare Glosar (ppm vs PPM):** Diferențierea case-sensitive în glosar și dicționar între `ppm` (unitate de măsură pentru concentrații) și `PPM` (biocidul *Plant Preservative Mixture*).
*   **Card Philodendron Interactiv:** Cardul speciilor în lucru trimite acum direct către Roadmap-ul public pentru transparența dezvoltării.

### v0.1.1 — Structură Hub & Standardizare
*Data: 24 Mai 2026*

*   **Standardizare Metadate:** Toate protocoalele existente au acum metadate YAML standardizate (`status: literatura`, `hormoni`, `ultima_actualizare`, `versiune`).
*   **Badge-uri Vizuale în Layout:** Am integrat în layout-ul de protocol (`_layouts/protocol.html`) o bară de etichete colorate sub titlu. Aceasta afișează automat nivelul de dificultate (cu culori specifice: roșu pentru greu, galben pentru mediu, verde pentru ușor), categoria, statusul validării (cu nuanțe de violet, albastru, verde sau cyan), substanțele hormonale utilizate, data ultimei actualizări și versiunea protocolului.
*   **Jurnal de status public:** Lansarea acestei pagini (`status.md`) pentru a documenta versiunile și evoluția hub-ului.

### v0.1.0 — Fundație & Pregătire Site
*Data: 22 Mai 2026*

*   **Reparare Aprovizionare:** Înlocuirea tuturor linkurilor oarbe `(#)` din tabelul „Starter Pack” cu linkuri reale, directe către produse de la furnizori testați din România (eMag, DriedFruits, Ellemental, Dreamgrowshop, Savyprofessional, Med-Shop și Sticlărie Laborator). Am adăugat MS Media (MSP09) și am separat micropipetele și reglajele de pH.
*   **Ghidul „Start Aici”:** Crearea traseului de onboarding de 30-60 de minute pentru începători, bazat pe o cronologie (stepper) vizuală dinamică.
*   **Banner de Status Global:** Integrarea unui status global vizibil pe prima pagină și în sidebar (`STATUS: protocoale extrase din literatura | validare practica in curs.`).
*   **Modernizare Ghiduri:** Înlocuirea mesajului „WORK IN PROGRESS” din centralizatorul principal cu un text de bun venit prietenos.
*   **Configurare Crawler:** Crearea fișierului `robots.txt` și configurarea sitemap-ului XML pentru indexare web.
*   **Publicare Roadmap:** Crearea paginii `ROADMAP.md` direct pe site pentru transparența planurilor.
