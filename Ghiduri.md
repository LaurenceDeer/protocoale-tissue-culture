---
layout: default
title: Centralizator Ghiduri
description: "Ghiduri pas-cu-pas pentru tissue culture acasă. De la prepararea mediilor și sterilizare, la chimie, toxicologie și reducerea contaminării."
---

<style>
/* Stil interactiv pentru modulele de ghiduri */
summary {
  cursor: pointer;
  padding: 15px;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-left: 4px solid var(--accent-amber);
  border-radius: 4px;
  font-family: var(--font-heading);
  font-weight: 500;
  color: var(--text-main);
  margin-bottom: 10px;
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: space-between;
  transition: all 0.2s ease;
}

summary:hover {
  background-color: #0c120f;
  border-left-color: var(--accent-hover);
}

summary::after {
  content: "[+]";
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 0.9em;
  color: var(--accent-amber);
}

details[open] summary::after {
  content: "[-]";
}

summary::-webkit-details-marker {
  display: none;
}

details p, details ul {
  padding-left: 15px;
  border-left: 1px dashed var(--border-color);
  margin-left: 15px;
}
</style>

# 📚 Ghiduri Pas-Cu-Pas & Documentație Tehnică

Aici găsești manualele practice de laborator concepute special pentru cultivarea plantelor in vitro la tine acasă. Fără jargon inutil, fără teorii sterile — doar tehnici verificate pe care le poți aplica direct în bucătărie sau în mini-laboratorul tău.

Dacă ești complet la început de drum, îți recomandăm să începi cu traseul ghidat: **[🚀 Start Aici: Traseul Începătorului](./start-aici.html)**.

---

<details markdown="1">
  <summary><strong>Modulul 1: Fundamentele Practice (Pentru cine începe astăzi)</strong></summary>
    
Aici sunt noțiunile critice. Dacă le stăpânești pe acestea, elimini din start 90% din greșelile clasice de început:

* [🧊 Ghidul "Absolute Zero" (Primul tău borcan sub 200 RON)](./ghiduri/Absolute-Zero.html)
* [🧪 Prepararea Mediilor (Bucătăria Chimică)](./ghiduri/PreparareMedii.html)
* [🧮 Calculator de Medii & Hormoni (Interactiv)](./ghiduri/calculator.html)
* [📦 SAB vs. LFH (Cutia cu aer mort vs. Hota cu flux laminar)](./ghiduri/SABvsLFH.html)
* [☢️ Sterilizarea: Protocolul Zero](./ghiduri/Sterilizare.html)
  
</details>

<details markdown="1">
  <summary><strong>Modulul 2: Știința din Spate (Chimia și Biologia Hormonilor)</strong></summary>
  
Înțelege mecanismele biologice ca să nu mai lucrezi pe ghicite:

* [🧬 Reglatorii de Creștere (PGRs: Auxine, Citochinine și Rapoarte)](./ghiduri/PGRs.html)
* [🧪 Controlul pH-ului (De la calibrare la evitarea fenomenului de supică)](./ghiduri/pH.html)

</details>

<details markdown="1">
  <summary><strong>Modulul 3: Tehnici Aseptice & Finețuri de Laborator</strong></summary>
  
Detaliile care fac diferența dintre un borcan plin de lăstari sănătoși și o cultură compromisă de mucegai:

* [☠️ Toxicologie & Manipulare în Siguranță](./ghiduri/Manipulare-Inocuitate.html)
* [🦠 Reducerea Contaminării (Tehnica de lucru în SAB)](./ghiduri/Contaminarea.html)
* [✂️ Selecția Explantelor (Ce tai și de unde)](./ghiduri/Selecție-Explante.html)
* [🚨 Troubleshooting Vizual (Ghid de diagnoză a problemelor)](./ghiduri/Troubleshooting.html)
* [📋 Fișă de Lucru: Checklist Laborator (Print-Friendly)](./ghiduri/checklist-laborator.html)
* [📖 Dicționarul Biohackerului (Terminologie RO-EN)](./ghiduri/Dicționar.html)

</details>

<details markdown="1">
  <summary><strong>Modulul 4: Resurse & Comunitate</strong></summary>
  
Surse de documentare științifică, canale recomandate și ghidul de contribuție deschisă:

* [🛒 Aprovizionare & Echipament](./surse/Aprovizionare.html)
* [🔓 Acces la Lucrări Științifice (Sci-Hub)](./surse/SciHub.html)
* [📺 Canale YouTube Recomandate](./surse/youtubechannels.html)
* [🤖 Transparență AI (Despre Utilizarea AI pe Acest Site)](./surse/AI-Disclosure.html)
* [🤝 Ghid de Contribuție](./surse/CONTRIBUTING.html)

</details>
