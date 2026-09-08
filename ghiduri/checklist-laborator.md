---
layout: default
title: Fișă Checklist Laborator (Print-Friendly)
description: "Fișă de lucru și checklist de laborator pentru activitatea sterilă in vitro acasă. Imprimă și bifează pașii pentru siguranță și sterilitate maximă."
---

# 📋 Fișă de Lucru: Checklist de Laborator (Print-Friendly)

Această fișă este concepută pentru a fi **imprimată** și luată cu tine pe masa de lucru. Respectarea fiecărui pas de sterilitate reduce șansele de contaminare de la 80% la sub 5%.

*💡 **Sfat practic:** Poți lamina această pagină sau o poți introduce într-o folie transparentă de plastic, bifând căsuțele cu un marker nepermanent pentru a o reutiliza la fiecare sesiune.*

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

/* Optimizare pentru Imprimare */
@media print {
  body {
    background-color: white !important;
    color: black !important;
  }
  .sidebar, #search-container, footer, .comments-section, nav {
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
    <li><input type="checkbox"> <strong>Curățenia vaselor:</strong> Toate borcanele, paharele Berzelius, pensetele și bisturiele au fost spălate cu apă caldă și detergent.</li>
    <li><input type="checkbox"> <strong>Igienizarea suprafeței:</strong> Masa de lucru și blatul au fost curățate mecanic și șterse cu dezinfectant.</li>
    <li><input type="checkbox"> <strong>Stocul de apă distilată:</strong> Ai la îndemână minim 2–3 litri de apă distilată curată pentru preparare și clătiri sterile.</li>
    <li><input type="checkbox"> <strong>Echipamentul de protecție (EIP):</strong> Mănușile de nitril, masca de față și ochelarii de protecție sunt pregătite pe masă.</li>
  </ul>

  <h2>2. 🧪 Prepararea Mediilor & Autoclavarea</h2>
  <ul class="checklist-list">
    <li><input type="checkbox"> <strong>Cântărire precisă:</strong> Ai dizolvat doza de pudră MS (4.4 g/L), zahărul (30 g/L) și hormonii stoc în ~800 mL apă distilată.</li>
    <li><input type="checkbox"> <strong>Reglarea pH-ului (PAS CRITIC):</strong> Ai adus pH-ul la <strong>5.8</strong> cu KOH/HCl DUPĂ dizolvarea sărurilor, dar ÎNAINTE de adăugarea agarului.</li>
    <li><input type="checkbox"> <strong>Activarea agarului:</strong> Ai adăugat 6–8 g/L agar și ai încălzit amestecul până când lichidul a devenit complet limpede.</li>
    <li><input type="checkbox"> <strong>Turnarea în borcane:</strong> Ai turnat ~2–3 cm de mediu fierbinte în fiecare borcan.</li>
    <li><input type="checkbox"> <strong>Capace libere pe filet:</strong> Capacele borcanelor NU sunt strânse ermetic (lăsate un sfert de tură desfăcute ca să respire).</li>
    <li><input type="checkbox"> <strong>Venting la oală:</strong> Ai lăsat aburul să iasă liber din oala sub presiune timp de <strong>7–10 minute</strong> înainte de a pune greutatea pe valvă.</li>
    <li><input type="checkbox"> <strong>Sterilizare la 15 PSI:</strong> Ai menținut presiunea la 15 PSI (121°C) timp de <strong>15–20 de minute</strong>.</li>
    <li><input type="checkbox"> <strong>Răcire naturală & Înfiletare:</strong> Ai lăsat oala să se răcească complet fără decompresie forțată, iar la deschidere ai strâns rapid capacele.</li>
  </ul>

  <h2>3. 🧫 Organizarea în Still Air Box (SAB)</h2>
  <ul class="checklist-list">
    <li><input type="checkbox"> <strong>Dezinfectarea cutiei:</strong> Ai pulverizat generos pereții interiori și fundul SAB-ului cu alcool izopropilic (IPA 70%).</li>
    <li><input type="checkbox"> <strong>Pauza de evaporare (Anti-Flash Fire):</strong> Ai lăsat cutia deschisă 2–3 minute pentru dispersarea vaporilor inflamabili de alcool.</li>
    <li><input type="checkbox"> <strong>Mise en place complet:</strong> Ai introdus în SAB borcanele cu gel, pensetele, bisturiul, suportul de tăiere steril și borcanele cu apă sterilă.</li>
    <li><input type="checkbox"> <strong>Asepsia operatorului:</strong> Ai pus mănușile de nitril și le-ai frecat bine cu alcool 70% înainte de a introduce mâinile în cutie.</li>
  </ul>

  <h2>4. ✂️ Sterilizarea Explantului & Inocularea</h2>
  <ul class="checklist-list">
    <li><input type="checkbox"> <strong>Prespălare mecanică:</strong> Ai spălat explantele sub jet domol de apă de la chiuvetă cu detergent timp de 15 minute.</li>
    <li><input type="checkbox"> <strong>Dip în alcool:</strong> Ai trecut explantele timp de 10–30 secunde prin alcool 70%.</li>
    <li><input type="checkbox"> <strong>Baia de clor + surfactant:</strong> Ai scufundat piesele în soluția de clor de casă 10–20% cu 1 picătură de detergent, respectând timpul exact per specie.</li>
    <li><input type="checkbox"> <strong>Clătire triplă sterilă:</strong> Ai clătit piesele în 3 băi succesive de apă distilată sterilă în SAB.</li>
    <li><input type="checkbox"> <strong>Fasonare aseptică:</strong> Ai tăiat marginile arse de clor cu o lamă sterilă de bisturiu.</li>
    <li><input type="checkbox"> <strong>Regula unghiului de 45°:</strong> Ai deschis capacul borcanului doar parțial, fără a trece cu mâna peste gura recipientului, ai înfipt explantul și ai închis capacul etanș.</li>
  </ul>

  <h2>5. 🏷️ Post-Operare & Întreținere</h2>
  <ul class="checklist-list">
    <li><input type="checkbox"> <strong>Etichetare clară:</strong> Ai scris pe fiecare borcan specia, compoziția mediului și data inoculării.</li>
    <li><input type="checkbox"> <strong>Raft de creștere:</strong> Ai așezat borcanele la 22–25°C, sub iluminare LED de 16 ore lumină / 8 ore întuneric.</li>
    <li><input type="checkbox"> <strong>Curățenie finală:</strong> Ai evacuat soluțiile reziduale la chiuvetă lăsând apa rece să curgă din abundență și ai curățat cutia SAB.</li>
  </ul>

</div>
