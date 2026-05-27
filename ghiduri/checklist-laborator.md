---
layout: default
title: Fișă Checklist Laborator (Print-Friendly)
description: "Fișă de lucru și checklist de laborator pentru activitatea sterilă in vitro acasă. Imprimă și bifează pașii pentru siguranță și sterilitate."
---

# 📋 Fișă de Lucru: Checklist Laborator (Print-Friendly)

Această fișă este concepută pentru a fi **imprimată** și luată cu tine în zona de lucru (bucătărie sau laborator). Respectarea fiecărui pas de sterilitate reduce șansele de contaminare de la 80% la sub 5%. 

*💡 Sfat: Poți lamina această fișă și bifa pașii cu un marker nepermanent pentru a o reutiliza la fiecare ședință de lucru.*

---

<style>
.lab-checklist h2 {
  margin-top: 35px;
  color: var(--accent-amber);
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 8px;
  font-size: 1.3em;
  font-family: var(--font-heading);
  display: flex;
  align-items: center;
  gap: 10px;
}

.checklist-list {
  list-style: none;
  padding-left: 0;
  margin-bottom: 30px;
}

.checklist-list li {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 10px 15px;
  border-bottom: 1px dashed var(--border-color);
  transition: background-color 0.2s ease;
  line-height: 1.5;
}

.checklist-list li:hover {
  background-color: rgba(255, 176, 0, 0.02);
}

.checklist-list input[type="checkbox"] {
  margin-top: 3px;
  width: 18px;
  height: 18px;
  cursor: pointer;
  accent-color: var(--accent-amber);
  flex-shrink: 0;
}

.checklist-list strong {
  color: var(--text-main);
}

/* Print optimizations */
@media print {
  body {
    background-color: white !important;
    color: black !important;
  }
  .sidebar, #search-container, footer, .comments-section {
    display: none !important;
  }
  .main-content {
    margin-left: 0 !important;
    width: 100% !important;
    padding: 0 !important;
  }
  .lab-checklist h2 {
    color: black !important;
    border-bottom: 2px solid black !important;
    page-break-after: avoid;
    margin-top: 25px;
  }
  .checklist-list li {
    border-bottom: 1px solid #ccc !important;
    page-break-inside: avoid;
    padding: 8px 0;
  }
  .checklist-list input[type="checkbox"] {
    border: 1px solid black !important;
    outline: 1px solid black !important;
  }
}
</style>

<div class="lab-checklist">

  <h2>1. 📦 Pregătirea Spațiului & Instrumentarului</h2>
  <ul class="checklist-list">
    <li><input type="checkbox"> <strong>Materiale curate:</strong> Toate borcanele, caserolele PP, paharele de clătire și ustensilele au fost spălate cu apă caldă și detergent.</li>
    <li><input type="checkbox"> <strong>Curățenie primară:</strong> Suprafața de lucru exterioară (masa, blatul) a fost curățată fizic și ștearsă cu dezinfectant.</li>
    <li><input type="checkbox"> <strong>Pregătire lichide:</strong> Ai la îndemână apă distilată suficientă (minim 1-2 litri) și sticla cu spirt/alcool izopropilic 70%.</li>
    <li><input type="checkbox"> <strong>Echipament de siguranță:</strong> Masca de față, ochelarii de protecție și mănușile de nitril sunt pregătite și ușor accesibile.</li>
  </ul>

  <h2>2. 🌬️ Dezinfectarea SAB (Still Air Box)</h2>
  <ul class="checklist-list">
    <li><input type="checkbox"> <strong>Poziționare SAB:</strong> Cutia este așezată într-o cameră complet lipsită de curenți de aer (uși/ferestre închise, ventilatoare/AC oprite).</li>
    <li><input type="checkbox"> <strong>Umezire pereți:</strong> Interiorul cutiei (tavanul, pereții laterali, podeaua) a fost pulverizat generos cu alcool 70%. Lichidul trebuie lăsat pe pereți (acesta acționează ca o capcană fizică pentru spori).</li>
    <li><input type="checkbox"> <strong>Introducere unelte:</strong> Ustensilele metalice (pensete, bisturiu), paharele de sticlă pentru clătire și borcanele cu mediu au fost șterse cu spirt și introduse în cutie.</li>
    <li><input type="checkbox"> <strong>Stabilizare aer:</strong> S-a lăsat SAB-ul nemișcat timp de minim 5-10 minute înainte de începerea inoculării (pentru ca toți sporii din interior să se așeze și să se lipească de pereți).</li>
  </ul>

  <h2>3. 🧪 Prepararea & Sterilizarea Mediului</h2>
  <ul class="checklist-list">
    <li><input type="checkbox"> <strong>Cântărire precisă:</strong> Sărurile MS, sucroza, agarul și hormonii (dacă e cazul) au fost cântăriți pe cântarul de precizie (0.01g).</li>
    <li><input type="checkbox"> <strong>Ajustare pH:</strong> pH-ul a fost reglat la 5.7 - 5.8 folosind pH-metrul calibrat și soluții pH UP/DOWN, înainte de a topi agarul.</li>
    <li><input type="checkbox"> <strong>Dizolvare totală:</strong> Amestecul a fost încălzit până când agarul a devenit perfect limpede/transparent.</li>
    <li><input type="checkbox"> <strong>Turnare & Capace:</strong> Mediul a fost distribuit în borcane, iar capacele au fost puse și lăsate slab strânse (un sfert de tură înapoi) pentru a permite aburului să iasă.</li>
    <li><input type="checkbox"> <strong>Sterilizare presiune:</strong> Recipientele au fost sterilizate în oală sub presiune timp de 15-20 de minute la 15 PSI (sau conform manualului oalei/multicooker-ului).</li>
    <li><input type="checkbox"> <strong>Răcire sterilă:</strong> Capacele au fost strânse imediat după depresurizare completă (folosind mănuși), iar borcanele au fost așezate în SAB sau într-un loc curat pentru solidificare.</li>
  </ul>

  <h2>4. 🔬 Inocularea (Lucrul steril în SAB)</h2>
  <ul class="checklist-list">
    <li><input type="checkbox"> <strong>Igienă personală:</strong> Mâinile și antebrațele sunt spălate cu săpun antibacterian și pulverizate din abundență cu alcool 70%. Mănușile sunt pulverizate repetat în timpul lucrului.</li>
    <li><input type="checkbox"> <strong>Sterilizare chimică explant:</strong> Planta/explantul este spălat de pământ și scufundat în soluția de clor + Tween 20 conform timpului exact din protocolul specific speciei.</li>
    <li><input type="checkbox"> <strong>Clătiri succesive:</strong> Explantul sterilizat este mutat exclusiv cu penseta sterilă prin 3 pahare succesive de apă distilată sterilă în interiorul SAB-ului.</li>
    <li><input type="checkbox"> <strong>Mișcări controlate:</strong> Lucrezi încet, direct în centrul SAB-ului. Evită să treci mâinile deasupra recipientelor deschise și nu vorbi deasupra deschizăturilor.</li>
    <li><input type="checkbox"> <strong>Ustensile sterile fierbinți:</strong> Bisturiul și penseta sunt trecute prin sterilizatorul cu cuarț (sau spălate cu alcool și uscate) între fiecare utilizare și răcite înainte de a atinge explantul.</li>
  </ul>

  <h2>5. 🧼 Curățenie & Monitorizare post-lucru</h2>
  <ul class="checklist-list">
    <li><input type="checkbox"> <strong>Etichetare clară:</strong> Toate borcanele inoculate au fost etichetate (Specie, Data, Rețeta/Hormoni, Status inițial).</li>
    <li><input type="checkbox"> <strong>Curățare instrumentar metalic:</strong> Bisturiul și pensetele sunt spălate, uscate complet (pentru a evita rugina) și depozitate corespunzător.</li>
    <li><input type="checkbox"> <strong>Raft de incubație:</strong> Borcanele sunt plasate sub lumini de creștere la temperaturi stabile (de preferat 22-26°C), departe de lumina directă a soarelui.</li>
    <li><input type="checkbox"> <strong>Monitorizare infecții:</strong> Verifici borcanele zilnic timp de 2 săptămâni. Orice borcan care prezintă puf de mucegai sau colonii bacteriene este izolat și evacuat imediat pentru a nu infecta restul lotului.</li>
  </ul>

</div>
