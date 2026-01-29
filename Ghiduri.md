<style>
/* Asta transformă textul simplu într-un card sexy */
summary {
  cursor: pointer; /* Face cursorul să devină mână (Hand icon) */
  padding: 15px; /* Îi dă aer să respire */
  background-color: #21262d; /* Culoare de fundal (Gri închis GitHub style) */
  border: 1px solid #30363d; /* Bordură subtilă */
  border-left: 5px solid #d29922; /* Linia aia portocalie șmecheră în stânga */
  border-radius: 6px; /* Colțuri rotunjite */
  font-weight: bold; /* Text gros */
  color: #c9d1d9; /* Culoare text */
  margin-bottom: 10px; /* Spațiu între butoane */
  list-style: none; /* Ascunde săgeata aia urâtă default */
  display: flex; /* Aliniere modernă */
  align-items: center;
  justify-content: space-between;
}

/* Asta se întâmplă când pui mouse-ul pe el */
summary:hover {
  background-color: #30363d; /* Se luminează puțin */
  border-left-color: #f2cc60; /* Portocaliul devine mai aprins */
}

/* Hack pentru a pune o săgeată custom în dreapta */
summary::after {
  content: "🔽"; 
  font-size: 1.2em;
}

/* Când e deschis, schimbăm săgeata */
details[open] summary::after {
  content: "🔼";
}

/* Ascundem săgeata default a browserului (că e urâtă) */
summary::-webkit-details-marker {
  display: none;
}
</style>
### WORK IN PROGRESS
Aici o să pun linkurile către ghidurile pe care le compun, iar pagina prezentă este o metodă de centralizare.

---

<details markdown="1">
  <summary><strong>Modulul 1: Chestiile de bază - pentru cine incepe astăzi.</strong></summary>
    <br>
  
Astea sunt lucruri critice, fără să le stăpânești, ai șanse mari să eșuezi și să te intrebi "DE CE MI-O MURIT ORHIDEEA DE 100 DE LEI"

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
* [Terminologie-Dicționar](/ghiduri/Dicționar.md)

</details>

<details markdown="1">
  <summary><strong>Modulul 4: Resurse (Meta-Learning)</strong></summary>
  
Aici vor fi surse de informare de unde și eu mă informez pentru a vă aduce informațiile pe acest website.

* [Reviste Științifice și Publicații](./surse/researchlinks.md)
* [Sci-Hub Stuff (IYKYK)](./surse/SciHub.md)
* [Cărți + PDF-uri](./surse/Cărți.md)
* [Canale de Youtube](./surse/youtubechannels.md)

  </details>
