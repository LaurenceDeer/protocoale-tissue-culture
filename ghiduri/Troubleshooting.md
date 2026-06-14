---
layout: default
title: Troubleshooting Vizual
description: "Identifică și rezolvă cele mai comune probleme în clonarea plantelor in vitro: contaminare, vitrificare, fenolizare și stagnare."
---

# 🚨 Troubleshooting Vizual (Ce a mers prost?)

Ai făcut totul "ca la carte", dar borcanul tău arată ca un experiment științific ratat. Nu te panica. Contaminarea și eșecurile fac parte din proces (chiar și în laboratoarele profesionale se aruncă o grămadă de borcane, stai să vezi videoclipul de la PlantsInJars unde a aruncat zeci..).

Folosește acest ghid pentru a identifica inamicul și a afla unde trebuie să îți îmbunătățești tehnica.

<pre class="mermaid" style="background-color: var(--bg-card); border: 1px solid var(--border-color); border-radius: 6px; padding: 20px; margin: 30px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.35); text-align: center; font-family: inherit;">
graph LR
    Start["🔍 Identificare Problemă"] --> Contaminare["Contaminare (pe gel/planta)"]
    Start --> ProblemePlanta["Probleme dezvoltare plantă"]

    Contaminare --> Fungal["A. Mucegai / Puf"]
    Contaminare --> Bacterial["B. Pete lăptoase / Zmârcâială"]

    ProblemePlanta --> Innegrire["A. Înnegrire (Fenolizare)"]
    ProblemePlanta --> Translucid["B. Aspect sticlos (Vitrificare)"]
    ProblemePlanta --> Stagnare["C. Nu crește (Stagnare)"]

    click Fungal "#mucegai" "Mergi la secțiune"
    click Bacterial "#bacterii" "Mergi la secțiune"
    click Innegrire "#fenolizare" "Mergi la secțiune"
    click Translucid "#vitrificare" "Mergi la secțiune"
    click Stagnare "#stagnare" "Mergi la secțiune"
</pre>

---

## 🦠 1. Inamicul Principal: Contaminarea

Dacă e de rău, se întâmplă de obicei în primele 3-7 zile.

### A. "Puful" (Mucegai / Contaminare Fungală) {#mucegai}
**Cum arată:** Puf alb, verde, negru sau roz care crește pe gel sau direct pe explant. Arată ca mucegaiul de pe pâinea lăsată prea mult pe masă.

![Contaminare fungală in vitro]({{ '/assets/images/mucegai.png' | relative_url }})
*Fig 1. Contaminare fungală (mucegai) pe mediu de cultură. Sursă: [r/PlantedTank (Reddit)](https://www.reddit.com/r/PlantedTank/comments/m54mcq/suggestion_for_treating_mold_in_tissue_culture/)*
**Sursa:** Aerul. Mucegaiul se răspândește prin spori purtați de curenții de aer.
**Unde ai greșit:**
- Nu ai folosit corect SAB-ul (ai mișcat prea repede mâinile și ai creat curenți de aer).
- Ai lăsat capacul borcanului deschis prea mult timp.
- Nu te-ai spălat pe mâini / nu ai dat cu suficient alcool pe mănuși și în cutie.
- Borcanele nu se închid ermetic.

### B. "Laptele / Zmârcâiala" (Contaminare Bacteriană) {#bacterii}
**Cum arată:** Pete lăptoase, tulburi, galbene sau albe, care "curg" sau se întind pe gel. De multe ori pornesc exact de la baza plantei (explantului). Miros foarte urât dacă deschizi borcanul.

![Contaminare bacteriană in vitro]({{ '/assets/images/bacterii.png' | relative_url }})
*Fig 2. Contaminare bacteriană cu aspect lăptos. Sursă: [PTCB (Journal)](https://doi.org/10.3329/ptcb.v28i1.37202)*
**Sursa:** Planta în sine sau instrumentele insuficient sterilizate.
**Unde ai greșit:**
- Protocolul de sterilizare a plantei (clor/înălbitor) a fost prea scurt sau prea slab.
- Nu ai sterilizat corect penseta/bisturiul între tăieturi.
- Explantul a fost prea murdar de la început (luat dintr-o zonă cu pământ/praf).

> [!CAUTION]
> **Soluția universală pentru contaminare:** Nu încerca să "salvezi" planta. Riscul de a împrăștia sporii în tot SAB-ul tău este prea mare. Sterilizează borcanul la autoclav (cu tot cu ce e în el) ca să ucizi monștrii, apoi curăță-l și ia-o de la capăt cu o plantă nouă.

---

## 🥀 2. Planta "Plânge" sau se Înnegrește (Fenolizare) {#fenolizare}

**Cum arată:** Gelul din jurul plantei se face maro închis sau negru. Baza plantei se usucă și se înnegrește.

![Fenolizare in vitro]({{ '/assets/images/fenolizare.png' | relative_url }})
*Fig 3. Fenolizare (browning) - oxidarea și înnegrirea mediului din cauza secreției de compuși fenolici. Sursă: [Lab Associates](https://labassociates.com/browning-in-tissue-culture-media)*
**Ce se întâmplă:** Când ai tăiat planta cu bisturiul, ea a "strigat" după ajutor eliberând compuși fenolici (un mecanism de apărare natural). În natură, acești compuși o apără. În borcan, fiind un spațiu închis, planta se otrăvește singură cu ei.
**Cum previi:**
- Folosește un bisturiu extrem de ascuțit (taie ferm, nu "mesteca" și nu strivi tulpina).
- Ține explantul în apă distilată sterilă până îl pui în borcan.
- *Remediu:* Dacă observi înnegrirea în primele zile, scoate planta rapid în SAB, taie 1 mm din partea neagră și mut-o pe un mediu nou, curat (subcultură).

---

## 💧 3. Planta "de Sticlă" (Vitrificare / Hiperhidrare) {#vitrificare}

**Cum arată:** Frunzele devin groase, fragile, apoase, translucide. Planta pare "umflată" cu apă și are un aspect de sticlă mată. 
**Ce se întâmplă:** Aerul din borcan are 100% umiditate. Uneori, stomatele plantei (porii prin care respiră) se dau peste cap, iar planta începe să absoarbă incontrolabil lichid din gel. Nu mai face fotosinteză și în cele din urmă se "îneacă".
**Cum previi / remediezi:**
- **Prea mult hormon (Citokinină):** Dacă rețeta ta are prea mult BAP/Kinetin, planta "o ia razna". Scade concentrația.
- **Prea multă umiditate:** Folosește capace care permit un minim de schimb de gaze (de exemplu, capace cu filtru microporos).
- **Prea puțin Agar:** Dacă gelul este prea moale (mai mult lichid decât gel), mărește cantitatea de Agar cu 1-2 grame/litru.
- *Remediu:* Scade umiditatea lăsând borcanul într-o zonă puțin mai rece, ca condensul să se formeze pe pereți, nu pe plantă.

---

## 🐌 4. Planta refuză să crească (Stagnare) {#stagnare}

**Cum arată:** Ai o plantă perfect verde, curată, fără mucegai... dar care stă de 2 luni și nu crește nicio frunză.
**Unde e problema:**
- **Mediul e greșit:** Poate planta urăște rețeta MS 100% și preferă Half-MS (1/2).
- **Hormoni:** Poate ai pus doar Auxine, iar planta a făcut doar rădăcini, ignorând complet partea de sus.
- **pH incorect:** Ai verificat pH-ul înainte să torni gelul? Dacă e prea acid (< 5.0) sau prea alcalin (> 6.0), planta nu poate trage nutrienții din gel, chiar dacă ei sunt acolo! (Vezi [Ghidul pH-ului](./pH.md)).

<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    mermaid.initialize({
      startOnLoad: true,
      theme: 'dark',
      themeVariables: {
        background: '#0D0D0D',
        primaryColor: '#FFB000',
        primaryTextColor: '#E0E0E0',
        lineColor: '#1A1A1A'
      }
    });
  });
</script>
