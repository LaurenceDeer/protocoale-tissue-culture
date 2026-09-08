---
layout: default
title: Troubleshooting Vizual
description: "Identifică și rezolvă rapid problemele din culturile in vitro: contaminare fungală și bacteriană, oxidare fenolică, vitrificare și stagnare."
---

# 🚨 Troubleshooting Vizual: Ce a Mers Greșit?

> *„Eșecurile și borcanele compromise fac parte integrantă din procesul de învățare. Până și cele mai mari laboratoare de cercetare din lume aruncă periodic culturi contaminate.”*

Nu intra în panică dacă un borcan nu arată perfect. Folosește această diagramă și ghidul vizual de mai jos pentru a identifica rapid cauza exactă și a-ți regla tehnica pentru tura următoare.

<pre class="mermaid" style="background-color: var(--bg-card); border: 1px solid var(--border-color); border-radius: 6px; padding: 20px; margin: 30px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.35); text-align: center; font-family: inherit;">
graph LR
    Start["🔍 Identificare Problemă"] --> Contaminare["1. Contaminare (pe gel/plantă)"]
    Start --> ProblemePlanta["2. Probleme de Fiziologie"]

    Contaminare --> Fungal["A. Mucegai / Puf (Fungic)"]
    Contaminare --> Bacterial["B. Pete Lăptoase / Zmârcâială (Bacterian)"]

    ProblemePlanta --> Innegrire["A. Înnegrire Gel / Bază (Fenolizare)"]
    ProblemePlanta --> Translucid["B. Aspect Sticlos / Apoasă (Vitrificare)"]
    ProblemePlanta --> Stagnare["C. Nu Crește Deloc (Stagnare)"]

    click Fungal "#mucegai" "Mergi la secțiune"
    click Bacterial "#bacterii" "Mergi la secțiune"
    click Innegrire "#fenolizare" "Mergi la secțiune"
    click Translucid "#vitrificare" "Mergi la secțiune"
    click Stagnare "#stagnare" "Mergi la secțiune"
</pre>

---

## 🦠 1. Inamicul Numărul 1: Contaminarea

Dacă este vorba de o contaminare externă, primele semne devin vizibile de regulă în primele **3–7 zile** de la inoculare.

### A. „Puful” (Contaminare Fungală / Mucegai) {#mucegai}

**Cum arată:** Puf fin alb, verde, negru, cenușiu sau roz care se dezvoltă pe suprafața gelului sau direct pe frunze.

![Contaminare fungală in vitro]({{ '/assets/images/mucegai.png' | relative_url }})
*Fig 1. Colonie fungică (mucegai) dezvoltată pe mediul nutritiv.*

* **Sursa principală:** Aerul din încăpere. Ciupercile se reproduc prin spori microscopici transportați de curenții de aer.
* **Unde a apărut breșa:**
  * Mișcări prea rapide ale mâinilor în SAB, care au aspirat aer din cameră.
  * Capacul borcanului a fost ținut deschis prea mult timp în timpul inoculării.
  * Ai trecut cu mâna sau cu o pensetă nesterilizată pe deasupra borcanului deschis.
  * Borcanul nu a fost închis etanș după inoculare.

---

### B. „Laptele sau Zmârcâiala” (Contaminare Bacteriană) {#bacterii}

**Cum arată:** Pelicule lăptoase, vâscoase, albe sau galbene care curg pe suprafața gelului, adesea pornind fix de la baza tăieturii explantului. Pot avea un miros neplăcut.

![Contaminare bacteriană in vitro]({{ '/assets/images/bacterii.png' | relative_url }})
*Fig 2. Contaminare bacteriană cu aspect umed și lăptos.*

* **Sursa principală:** Planta în sine (bacterii din crăpăturile epidermei) sau unelte metalice nesterilizate la cald între tăieturi.
* **Unde a apărut breșa:**
  * Baia de clor a fost prea scurtă sau soluția a fost prea diluată.
  * Nu ai adăugat detergent ca surfactant, iar clorul a ocolit sporii ascunși printre perișori.
  * Vârful bisturiului nu a fost răcit suficient după sterilizare și a ars țesutul, deschizând calea bacteriilor.

> [!CAUTION]
> **Ce faci cu borcanele contaminate:** Nu încerca să „cureți” sau să speli o plantă deja contaminată în SAB, altfel vei elibera spori în tot spațiul de lucru! Bagă borcanul cu capacul închis în oala sub presiune timp de 15 minute la 121°C pentru a neutraliza patogenii, apoi spală-l și ia-o de la capăt.

---

## 🥀 2. Fenolizarea (Înnegrirea Mediului și a Bazei Plantei) {#fenolizare}

**Cum arată:** Gelul din jurul explantului devine maro închis sau negru ca smoala în primele zile, iar baza tăiată a plantei se necrozează.

![Fenolizare in vitro]({{ '/assets/images/fenolizare.png' | relative_url }})
*Fig 3. Fenolizare (browning) cauzată de oxidarea compușilor polifenolici secretați de plantă.*

* **Mecanism biologic:** Rănirea plantei la tăiere declanșează un răspuns de apărare prin eliberarea de compuși polifenolici. Într-un recipient închis, acești compuși oxidează și devin toxici pentru celulele plantei.
* **Cum previi și remediezi:**
  * Folosește întotdeauna o **lamă de bisturiu nouă și foarte ascuțită** (fă tăieturi netede, fără a strivi tulpina).
  * Adaugă **100 mg/L Acid Ascorbic** sau **1–2 g/L Cărbune Activ** în mediul de cultură.
  * *Măsură imediată:* Transferă explantul pe un **borcan nou cu mediu curat la fiecare 7–10 zile** în prima lună.

---

## 💧 3. Vitrificarea (Aspectul Sticlos / Hiperhidrarea) {#vitrificare}

**Cum arată:** Frunzele devin groase, translucide, fragile și arată ca îmbibate excesiv cu apă (aspect de sticlă mată).

* **Mecanism biologic:** Umiditatea de 100% din borcan combinată cu doze prea mari de citochinine (BAP) dereglează porii foliari (stomatele). Planta absoarbe apă necontrolat și își reduce capacitatea de a sintetiza clorofilă.
* **Cum previi și remediezi:**
  * **Scade concentrația de citochinine (BAP):** Concentrațiile prea mari declanșează vitrificarea.
  * **Mărește doza de agar:** Un gel prea moale favorizează hiperhidrarea. Adaugă încă 1.0–1.5 g/L agar.
  * Folosește capace care permit un schimb minim de gaze (cu membrană microporoasă) sau ține borcanele într-o zonă cu temperatură stabilă pentru a evita condensul masiv pe plantă.

---

## 🐌 4. Stagnarea (Planta Verde Care Nu Crește) {#stagnare}

**Cum arată:** Planta rămâne perfect verde și curată luni de zile, dar nu produce niciun lăstar nou și nicio rădăcină.

* **Cauze frecvente:**
  * **pH incorect:** Dacă pH-ul a fost reglat sub 5.2 sau peste 6.0, microelementele sunt blocate chimic (*Nutrient Lockout*), iar planta nu se poate hrăni.
  * **Profil hormonal neadaptat:** Planta are nevoie de un impuls de citochinine (BAP) pentru a rupe starea de latență a mugurilor dormanzi.
  * **Mediu prea concentrat:** Unele specii (orhidee, plante carnivore) stagnează pe MS complet și cer formulă diluată (**Half-MS** sau **WPM**).

<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
