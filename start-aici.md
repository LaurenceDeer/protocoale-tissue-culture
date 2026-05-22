---
layout: default
title: Start Aici — Traseul Începătorului
description: "Ești la primul tău borcan? Pornește pe traseul de 30-60 de minute conceput special pentru începători în micropropagare."
---

# 🚀 Start Aici: Traseul Începătorului

Dacă micropropagarea (clonarea in vitro) îți pare complexă sau plină de termeni tehnici, ai ajuns unde trebuie. Am conceput un traseu simplu, de **30–60 de minute**, care te va trece de la zero la primul tău borcan steril, echipat cu tot ce ai nevoie pentru a nu da greș.

Urmează pașii de mai jos în ordine:

<style>
.start-timeline {
  position: relative;
  max-width: 800px;
  margin: 40px auto;
  padding: 0 10px;
}

.start-timeline::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 30px;
  width: 2px;
  background: var(--border-color);
}

.start-step {
  position: relative;
  display: flex;
  margin-bottom: 45px;
}

.start-step:last-child {
  margin-bottom: 0;
}

.step-num {
  position: relative;
  z-index: 2;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: var(--bg-main);
  border: 2px solid var(--accent-amber);
  color: var(--accent-amber);
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 1.1em;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 0 12px rgba(255, 176, 0, 0.25);
}

.step-content {
  margin-left: 25px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  padding: 24px;
  flex-grow: 1;
  transition: all 0.25s ease;
}

.start-step:hover .step-content {
  border-color: var(--accent-amber);
  background-color: #0c120f; /* O nuanță foarte fină de verde bio */
  box-shadow: 0 4px 20px rgba(0,0,0,0.4);
}

.step-content h3 {
  margin-top: 0;
  margin-bottom: 10px;
  font-size: 1.3em;
  color: var(--text-main);
}

.step-content p {
  color: var(--text-muted);
  font-size: 0.95em;
  margin-bottom: 20px;
  line-height: 1.6;
}

.step-btn {
  display: inline-block;
  background-color: transparent;
  border: 1px solid var(--border-color);
  color: var(--text-main) !important;
  padding: 10px 20px;
  border-radius: 4px;
  font-weight: 600;
  font-size: 0.9em;
  text-decoration: none !important;
  transition: all 0.2s ease;
}

.step-btn:hover {
  background-color: var(--accent-amber);
  border-color: var(--accent-amber);
  color: var(--bg-main) !important;
}

.btn-amber {
  border-color: var(--accent-amber);
  color: var(--accent-amber) !important;
}

.btn-amber:hover {
  background-color: var(--accent-amber);
  color: var(--bg-main) !important;
}

@media (max-width: 768px) {
  .start-timeline::before {
    left: 20px;
  }
  .step-num {
    width: 34px;
    height: 34px;
    font-size: 0.95em;
  }
  .step-content {
    margin-left: 15px;
    padding: 18px;
  }
}
</style>

<div class="start-timeline">

  <!-- Pasul 1 -->
  <div class="start-step">
    <div class="step-num">1</div>
    <div class="step-content">
      <h3>⚠️ Siguranța & Aspectele Legale</h3>
      <p>Înainte de a porni oala sub presiune sau de a te juca cu alcoolul izopropilic și focul deschis, este esențial să înțelegi riscurile. Află, de asemenea, ce înseamnă Plant Breeders' Rights (PBR) pentru a clona responsabil și doar în scop personal.</p>
      <a class="step-btn" href="./surse/Avertisment.html">🔗 Citește Avertismentul de Siguranță</a>
    </div>
  </div>

  <!-- Pasul 2 -->
  <div class="start-step">
    <div class="step-num">2</div>
    <div class="step-content">
      <h3>🧊 Primul Tău Borcan (Fără Investiții Scumpe)</h3>
      <p>Începe cu tehnica "Absolute Zero" în bucătărie. Vei folosi o cutie de plastic simplă (SAB) ca spațiu steril, un agent de gelifiere comun (agar-agar de prăjituri) și zahăr. Scopul este să vezi dacă poți menține un mediu curat timp de 7-10 zile fără ca mucegaiul să apară.</p>
      <a class="step-btn" href="./ghiduri/Absolute-Zero.html">🧊 Începe Ghidul "Absolute Zero"</a>
    </div>
  </div>

  <!-- Pasul 3 -->
  <div class="start-step">
    <div class="step-num">3</div>
    <div class="step-content">
      <h3>🧪 Prepararea Mediului Rezonabil (MS)</h3>
      <p>Odată ce ai stăpânit tehnica de bază, trecem la nivelul următor: mediul complet Murashige & Skoog (MS). Aici vei învăța ordinea dizolvării ingredientelor, ajustarea riguroasă a pH-ului la 5.7 - 5.8 și sterilizarea prin autoclavare în oala sub presiune.</p>
      <a class="step-btn" href="./ghiduri/PreparareMedii.html">🧪 Învață Prepararea Mediilor</a>
    </div>
  </div>

  <!-- Pasul 4 -->
  <div class="start-step">
    <div class="step-num">4</div>
    <div class="step-content">
      <h3>🧮 Calculatorul Interactiv de Medii & Hormoni</h3>
      <p>Dozarea hormonilor (BAP, NAA, IBA) în micro-grame pe litru poate fi complicată și predispune la greșeli. Folosește calculatorul nostru interactiv conceput special pentru a-ți genera rețeta în funcție de volumul și diluțiile pe care le folosești.</p>
      <a class="step-btn btn-amber" href="./ghiduri/calculator.html">🧮 Deschide Calculatorul de Medii</a>
    </div>
  </div>

  <!-- Pasul 5 -->
  <div class="start-step">
    <div class="step-num">5</div>
    <div class="step-content">
      <h3>🌱 Primul Tău Protocol: Drosera Spatulata</h3>
      <p>Ești gata pentru prima ta cultură reală in vitro. Drosera (Roua Cerului) este planta de antrenament ideală: semințele se sterilizează extrem de ușor în clor diluat, germinează rapid direct în borcan și produce zeci de clone mici pe care le poți diviza ulterior.</p>
      <a class="step-btn" href="./protocoale/drosera.html">🌱 Vezi Protocolul Drosera</a>
    </div>
  </div>

</div>

---

> [!TIP]
> * Pe parcursul călătoriei tale, ține mereu la îndemână secțiunea de **[Echipament & Aprovizionare](./surse/Aprovizionare.html)** pentru a ști exact de unde poți cumpăra unelte calitative de pe piața din România la cele mai bune prețuri.
> * De asemenea, poți urmări în timp real progresul dezvoltării acestui hub direct pe pagina **[Plan de Dezvoltare & Roadmap](./ROADMAP.html)**.
