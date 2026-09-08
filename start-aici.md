---
layout: default
title: Start Aici — Traseul Începătorului
description: "Ești la primul tău borcan? Pornește pe traseul de 30-60 de minute conceput special pentru începători în micropropagare."
---

# 🚀 Start Aici: Traseul Începătorului

Dacă ai aterizat aici și crezi că tissue culture înseamnă doar cercetători în halate albe care se uită în microscoape de 10.000€, respiră adânc. Se poate face lejer la tine în bucătărie sau în debara, fără să-ți vinzi un rinichi.

Traseul de mai jos e gândit să te treacă prin pașii esențiali fără să te înece în teorie inutilă. Ia-le în ordine, nu sări peste sterilizare (că altfel plângi după aia când vezi mucegaiul) și hai să scoatem primul tău borcan pe bune.

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
      <h3>⚠️ Siguranța & Bunul Simț (Să nu-ți dai foc la bucătărie)</h3>
      <p>Oala sub presiune la 15 PSI e o bombă mică dacă nu știi ce faci cu ea, iar vaporii de alcool izopropilic lângă o flacără deschisă nu iartă pe nimeni. Citește rapid avertismentul ca să știi ce chimicale să NU combini niciodată (gen clor cu oțet sau alcool) și cum stă treaba cu brevetele (PBR) ca să clonezi liniștit pentru tine acasă.</p>
      <a class="step-btn" href="./surse/Avertisment.html">🔗 Citește Avertismentul de Siguranță</a>
    </div>
  </div>

  <!-- Pasul 2 -->
  <div class="start-step">
    <div class="step-num">2</div>
    <div class="step-content">
      <h3>🧊 Primul Tău Borcan: Ghidul "Absolute Zero"</h3>
      <p>Nu te arunca să cumperi chimicale scumpe din prima zi. Faci o cutie transparentă de plastic cu două găuri pentru mâini (SAB), iei agar de la supermarket, puțin zahăr și vezi dacă ești capabil să ții un borcan curat 7-10 zile. Dacă nu-ți crește o pădure de mucegai în el, felicitări: ai mână sterilă și poți trece la plante reale.</p>
      <a class="step-btn" href="./ghiduri/Absolute-Zero.html">🧊 Începe Ghidul "Absolute Zero"</a>
    </div>
  </div>

  <!-- Pasul 3 -->
  <div class="start-step">
    <div class="step-num">3</div>
    <div class="step-content">
      <h3>🧪 Prepararea Mediilor (Bucătăria Chimică)</h3>
      <p>Dacă borcanele de test au ieșit curate, trecem la „carnea și cartofii” micropropagării: mediul Murashige & Skoog (MS). Aici vezi rețeta pas cu pas, de ce trebuie neapărat reglat pH-ul la 5.8 (altfel nu se leagă gelul și planta moare de foame) și cum gătești borcanele în oala sub presiune fără să le spargi capacele.</p>
      <a class="step-btn" href="./ghiduri/PreparareMedii.html">🧪 Învață Prepararea Mediilor</a>
    </div>
  </div>

  <!-- Pasul 4 -->
  <div class="start-step">
    <div class="step-num">4</div>
    <div class="step-content">
      <h3>🧮 Calculatorul de Medii (Să nu-ți prinzi urechile în miligrame)</h3>
      <p>Să calculezi 0.18 mg/L de hormon dintr-o soluție stoc de 1 mg/mL fără să greșești virgula e rețeta perfectă pentru dureri de cap. Am făcut un calculator interactiv moca pe site: bagi volumul de mediu pe care vrei să-l prepari și-ți zice exact câți mililitri de soluție stoc tragi cu seringa sau micropipeta.</p>
      <a class="step-btn btn-amber" href="./ghiduri/calculator.html">🧮 Deschide Calculatorul de Medii</a>
    </div>
  </div>

  <!-- Pasul 5 -->
  <div class="start-step">
    <div class="step-num">5</div>
    <div class="step-content">
      <h3>🌱 Prima Plantă: Drosera (Cea mai iertătoare)</h3>
      <p>Cea mai bună plantă pentru antrenament e <em>Drosera spatulata</em> (Roua Cerului). Semințele sunt extrem de rezistente și se spală ușor în clor fără să le distrugi, germinează rapid, nu cer niciun hormon (cresc de nebune pe MS simplu) și în 6 săptămâni ai zeci de mini-plante într-un singur recipient. E satisfacția de care ai nevoie ca să știi că metoda merge.</p>
      <a class="step-btn" href="./protocoale/drosera.html">🌱 Vezi Protocolul Drosera</a>
    </div>
  </div>

</div>

---

> [!TIP]
>
> * Ai nevoie de scule sau chimicale din România și nu știi de unde să le iei fără să plătești vama din SUA? Aruncă un ochi pe lista de **[Aprovizionare & Echipamente](./surse/Aprovizionare.html)**.
> * Dacă ești curios ce mai urmează să adaug pe site sau vrei să vezi ce specii sunt în lucru, verifică **[Roadmap-ul Public](./ROADMAP.html)**.
