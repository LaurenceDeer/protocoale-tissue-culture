<style>
/* Asta transformă textul simplu într-un card sexy */
summary {
  cursor: pointer;
  padding: 15px;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-left: 4px solid var(--accent-green);
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
  color: var(--accent-green);
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
### WORK IN PROGRESS
Aici o să pun linkurile către ghidurile pe care le compun, iar pagina prezentă este o metodă de centralizare.

---

<details markdown="1">
  <summary><strong>Modulul 1: Chestiile de bază - pentru cine incepe astăzi.</strong></summary>
    
Astea sunt lucruri critice, fără să le stăpânești, ai șanse mari să eșuezi și să te intrebi "DE CE MI-O MURIT ORHIDEEA DE 100 DE LEI"

* [Ghidul "Absolute Zero" (Primul Tău Borcan)](./ghiduri/Absolute-Zero.md)
* [Preparare Medii](./ghiduri/PreparareMedii.md)
* [SAB vs LFH](./ghiduri/SABvsLFH.md)
* [Sterilizare](./ghiduri/Sterilizare.md)
  
</details>

<details markdown="1">
  <summary><strong>Modulul 2: Știința din spate (Chimie și Biologie)</strong></summary>
  
Aici intră chestiile tehnice explicate de oameni de știință / cercetători în lucrările publicate pe site-uri de genul Researchgate. Bune de știut pentru curioși ca mine.

* [Reglatori de Creștere](./ghiduri/PGRs.md)
* [Controlul pH-ului](./ghiduri/pH.md)

</details>

<details markdown="1">
  <summary><strong>Modulul 3: Tehnici și soft skills (finețuri)</strong></summary>
  
Astea vor face diferența dintre amatori și pro-playeri

* [Tips and Tricks despre Manipulare: Inocuitate](./ghiduri/Manipulare-Inocuitate.md)
* [Reducerea Contaminării](./ghiduri/Contaminarea.md)
* [Selecția Explantelor](./ghiduri/Selecție-Explante.md)
* [Troubleshooting Vizual (Probleme și Soluții)](./ghiduri/Troubleshooting.md)
* [Terminologie-Dicționar](/ghiduri/Dicționar.md)

</details>

<details markdown="1">
  <summary><strong>Modulul 4: Resurse (Meta-Learning)</strong></summary>
  
Aici vor fi surse de informare de unde și eu mă informez pentru a vă aduce informațiile pe acest website.

* [Reviste Științifice și Publicații](./surse/researchlinks.md)
* [Sci-Hub Stuff (IYKYK)](./surse/SciHub.md)
* [Cărți + PDF-uri](./surse/Cărți.md)
* [Canale de Youtube](./surse/youtubechannels.md)
