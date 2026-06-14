---
layout: default
title: Protocoale & Specii
description: "Baza de date cu protocoale open-source de plant tissue culture. Rețete clare pentru sterilizare și medii pentru Monstera, Drosera, Philodendron și altele."
---

# 🧬 Baza de Date: Protocoale

Aici găsești rețetele exacte testate de comunitate pentru diferite specii. De la concentrația de clor pentru sterilizare, până la miligramele exacte de hormoni (BAP/NAA/IBA) folosite pentru a obține o cultură de succes.

<style>
.filter-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  padding: 15px 20px;
  margin-bottom: 30px;
  align-items: center;
}

.filter-group {
  display: flex;
  align-items: center;
  gap: 10px;
}

.filter-group label {
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 0.9em;
  color: var(--text-muted);
}

.filter-group select {
  background-color: var(--bg-main);
  border: 1px solid var(--border-color);
  color: var(--text-main);
  padding: 8px 12px;
  border-radius: 4px;
  font-family: var(--font-body);
  font-size: 0.9em;
  outline: none;
  cursor: pointer;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.filter-group select:hover, .filter-group select:focus {
  border-color: var(--accent-amber);
  box-shadow: 0 0 8px rgba(255, 176, 0, 0.15);
}

.home-card {
  transition: opacity 0.25s ease, transform 0.25s ease;
}

.card-hidden {
  display: none !important;
}
</style>

<div class="filter-container">
  <div class="filter-group">
    <label for="filter-category">📁 Categorie:</label>
    <select id="filter-category">
      <option value="all">Toate</option>
      <option value="carnivore">Carnivore</option>
      <option value="aroide">Aroide</option>
      <option value="conifere">Conifere</option>
      <option value="orhidee">Orhidee</option>
      <option value="gesneriaceae">Gesneriaceae</option>
      <option value="tropicale">Tropicale</option>
    </select>
  </div>

  <div class="filter-group">
    <label for="filter-difficulty">⏱️ Dificultate:</label>
    <select id="filter-difficulty">
      <option value="all">Toate</option>
      <option value="usoara">Ușoară</option>
      <option value="medie">Medie</option>
      <option value="grea">Grea</option>
    </select>
  </div>

  <div class="filter-group">
    <label for="filter-hormones">🧪 Hormoni:</label>
    <select id="filter-hormones">
      <option value="all">Toate</option>
      <option value="cu">Cu hormoni</option>
      <option value="fara">Fără hormoni</option>
    </select>
  </div>
</div>

<div class="home-grid">
  
  <div class="home-card" data-category="gesneriaceae" data-difficulty="usoara" data-hormones="cu">
    <a href="saintpaulia.html">
      <h2 style="color: var(--accent-amber);">🌸 Violetă Africană (Saintpaulia)</h2>
      <p>Gesneriaceae. Multiplicare prin organogeneză directă din fragmente de frunze cu BAP+NAA și înrădăcinare pe 1/2 MS. Nivel: Ușor.</p>
    </a>
  </div>

  <div class="home-card" data-category="carnivore" data-difficulty="medie" data-hormones="fara">
    <a href="drosera.html">
      <h2 style="color: var(--accent-amber);">🌱 Drosera (Roua Cerului)</h2>
      <p>Plantă carnivoră. Protocol complet pentru germinare in vitro și multiplicare. Nivel dificultate: Ușor/Mediu.</p>
    </a>
  </div>

  <div class="home-card" data-category="carnivore" data-difficulty="medie" data-hormones="cu">
    <a href="nepenthes.html">
      <h2 style="color: var(--accent-amber);">🩸 Pitcher Plant (Nepenthes)</h2>
      <p>Plantă carnivoră. Protocol pe mediu WPM cu cărbune activ pentru a preveni arderea rădăcinilor și secreția de fenoli. Nivel: Mediu.</p>
    </a>
  </div>

  <div class="home-card" data-category="aroide" data-difficulty="grea" data-hormones="cu">
    <a href="monstera.html">
      <h2 style="color: var(--accent-amber);">🌿 Monstera (Deliciosa / Thai) </h2>
      <p>Aroide. Protocol extragere muguri axilari, mediu cu citokinine (BAP) și aclimatizare biostimulată. Nivel: Greu.</p>
    </a>
  </div>

  <div class="home-card" data-category="tropicale" data-difficulty="medie" data-hormones="cu">
    <a href="musa.html">
      <h2 style="color: var(--accent-amber);">🍌 Bananier (Musa spp.)</h2>
      <p>Plantă tropicală. Multiplicare masivă pe mediu MS cu adaos de antioxidanți (acid ascorbic) și conservare la rece (15°C). Nivel: Mediu.</p>
    </a>
  </div>

  <div class="home-card" data-category="conifere" data-difficulty="medie" data-hormones="cu">
    <a href="thuja.html">
      <h2 style="color: var(--accent-amber);">🌲 Thuja Occidentalis (Tuia)</h2>
      <p>Coniferă ornamentală. Protocol fără hormoni cu rată de succes 100%. Nivel: Mediu.</p>
    </a>
  </div>

  <div class="home-card" data-category="orhidee" data-difficulty="grea" data-hormones="cu">
    <a href="phalaenopsis.html">
      <h2 style="color: var(--accent-amber);">🌸 Orhidee (Phalaenopsis)</h2>
      <p>Orhidee Moth. Multiplicare din noduri florale cu BAP+NAA sau germinare asimbiotică pe mediul Chen. Nivel: Greu.</p>
    </a>
  </div>

  <div class="home-card" data-category="aroide" data-difficulty="medie" data-hormones="cu" style="border-style: dashed;">
    <a href="../ROADMAP.html">
      <h2>🍀 Philodendron Pink Princess</h2>
      <p>În lucru (WIP). Teste de formare calus și regenerare directă a lăstarilor. <br><span style="color: var(--accent-amber); font-weight: 600;">[În lucru — Vezi planul/Roadmap]</span></p>
    </a>
  </div>

</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const catFilter = document.getElementById("filter-category");
  const diffFilter = document.getElementById("filter-difficulty");
  const hormFilter = document.getElementById("filter-hormones");
  const cards = document.querySelectorAll(".home-grid .home-card");

  function applyFilters() {
    const selectedCat = catFilter.value;
    const selectedDiff = diffFilter.value;
    const selectedHorm = hormFilter.value;

    cards.forEach(card => {
      const cardCat = card.getAttribute("data-category");
      const cardDiff = card.getAttribute("data-difficulty");
      const cardHorm = card.getAttribute("data-hormones");

      const matchCat = (selectedCat === "all" || cardCat === selectedCat);
      const matchDiff = (selectedDiff === "all" || cardDiff === selectedDiff);
      const matchHorm = (selectedHorm === "all" || cardHorm === selectedHorm);

      if (matchCat && matchDiff && matchHorm) {
        card.classList.remove("card-hidden");
      } else {
        card.classList.add("card-hidden");
      }
    });
  }

  catFilter.addEventListener("change", applyFilters);
  diffFilter.addEventListener("change", applyFilters);
  hormFilter.addEventListener("change", applyFilters);
});
</script>

<br>
<hr>

> **Ai un protocol care a funcționat perfect pentru tine?**  
> Fii parte din mișcare și ajută comunitatea! Vezi cum poți adăuga o rețetă nouă în <a href="{{ '/surse/CONTRIBUTING.html' | relative_url }}">Ghidul de Contribuție</a>.
