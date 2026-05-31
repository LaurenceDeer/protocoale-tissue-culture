---
layout: default
title: Cum să contribui
description: "Ghidul complet pentru a contribui la Open Tissue Culture RO. Află cum să adaugi protocoale, furnizori și resurse."
---

# Cum să contribui la Open Tissue Culture RO

> **Informația trebuie să fie liberă, accesibilă și colaborativă.**

Acest proiect este open-source. Orice pasionat de plante, biolog, sau hacker de garaj din România este binevenit să contribuie! Fie că ai reușit să clonezi cu succes o specie nouă și vrei să împarți protocolul, fie că ai găsit o greșeală gramaticală, ajutorul tău e super apreciat.

## 🤝 Cum poți ajuta?

1. **Adaugă Protocoale Noi:** Ai reușit să crești o Monstera Albo in vitro? Scrie protocolul! Folosește fișierul `protocoale/drosera.md` drept model. Ne interesează:
   - Rețeta de sterilizare (ex: 10% Clor pt 10 minute).
   - Rețeta mediului (ex: 1/2 MS, 20g Sucroză, 6g Agar).
   - Hormonii folosiți (PGRs) - dacă este cazul.
   
2. **Corectează și Completează:** Terminologia poate fi tricky. Dacă ești expert și vezi că o definiție din dicționar este incompletă, ajută-ne să o facem mai bună, păstrând totuși un limbaj non-academic, ușor de înțeles pentru toată lumea.

3. **Adaugă la lista de Aprovizionare:** Găsești Agar mai ieftin în altă parte? Cunoști o firmă de echipamente de laborator din RO care vinde și la persoane fizice? Adaugă linkul în `/surse/Aprovizionare.md`.

## 🛠️ Procesul tehnic (Cum trimiți modificări)

Dacă ești familiar cu GitHub, procesul este cel standard:

1. Dă **Fork** la acest repository.
2. Creează un branch nou pentru modificarea ta: `git checkout -b adaugat-protocol-monstera`.
3. Adaugă sau modifică fișierele Markdown (`.md`).
4. Fă commit cu o descriere clară: `git commit -m "Adăugat protocol pentru Monstera Deliciosa"`.
5. Dă **Push** la branch-ul tău.
6. Deschide un **Pull Request (PR)** către acest repository.

Dacă totul este în regulă, modificările tale vor fi vizibile pe site pentru toată lumea!

Dacă nu ești familiar cu GitHub, e ok, dă un mail și îți mulțumim din suflet pentru că îți pasă!

## 📜 Reguli de bun simț
- **Fără Paywall-uri sau Reclame:** Nu acceptăm linkuri de afiliere ascunse, reclame la produse minune sau cursuri plătite. Aici totul e gratis.
- **Păstrează tonul "casual":** Scopul este să facem știința accesibilă, nu să scriem teze de doctorat. Fără jargon inutil (iar unde îl folosim, îl explicăm).
- **Informație testată:** Te rog, postează doar protocoale pe care le-ai testat și care au funcționat pentru tine. Nu copia direct de pe internet fără să menționezi că e o traducere a unui studiu încă netestat.

Împreună transformăm sufrageriile din România în mini-laboratoare! 🧪🌿

---

## 📝 Șablon Standard pentru Protocol Nou

Pentru a propune un protocol nou, creează un fișier `.md` în folderul `protocoale/` folosind următorul șablon Markdown (copiază-l cu tot cu antetul dintre liniile `---`):

```markdown
---
layout: protocol
title: Protocol [Nume Comun Plantă] ([Nume Științific])
dificultate: [Ușoară / Medie / Grea]
categorie: [Carnivore / Aroide / Conifere / Orhidee / etc.]
status: literatura
hormoni: [Fără / BAP, NAA / IBA / etc.]
ultima_actualizare: AAAA-LL-ZZ
versiune: 1.0
---

# 🧬 Protocol Micropropagare: _[Nume Științific]_
**Bazat pe:** [Nume Autori (An) - ex: Popescu et al. (2024)]

| Parametru | Valoare Optimă (Conform Studii) |
| :--- | :--- |
| **Dificultate** | [Ușoară / Medie / Grea] |
| **Explant Recomandat** | [ex: Muguri axilari, fragmente de frunză, semințe] |
| **Mediu Multiplicare** | [ex: MS 100%, 1/2 MS] |
| **Hormoni (Multiplicare)**| [ex: 1.0 mg/L BAP + 0.1 mg/L NAA] |
| **pH** | [ex: 5.7 - 5.8] |
| **Timp Estimat** | [ex: Multiplicare: 30 zile \ Înrădăcinare: 30 zile] |
| **Rata Multiplicare** | [ex: ~5 lăstari / explant în 4 săptămâni] |

---

## 🧪 1. Prepararea Mediului (Ingrediente pentru 1 Litru)
1. **Săruri MS:** Doza completă (ex: 4.4 g/L) sau redusă.
2. **Zahăr (Sucroză):** 30 g/L (sau 20g/L).
3. **Agar / Gelifiant:** 7-8 g/L Agar (sau 2.5 g/L Gelrite).
4. **Hormoni (PGRs):** Se adaugă conform concentrației de mai sus din stocul preparat anterior.
5. **Ajustare pH:** Se reglează pH-ul la 5.7 - 5.8 folosind soluții de pH UP/DOWN înainte de a încălzi mediul pentru a topi agarul.
6. **Sterilizare:** Se sterilizează în oala sub presiune la 15 PSI timp de 15-20 de minute.

---

## 🧼 2. Sterilizarea Explantului (Procedura Chimică)
1. **Curățare fizică:** Spălare sub jet de apă cu detergent timp de ...
2. **Dezinfectare chimică:** Imersie în alcool 70% timp de ... secunde, urmată de imersie în clor diluat X% timp de ... minute.
3. **Clătire:** 3 spălări succesive în apă distilată sterilă în interiorul SAB-ului (câte 5 minute fiecare).

---

## 💡 3. Incubația și Creșterea
* **Lumină:** 16 ore lumină / 8 ore întuneric (LED rece/moderat).
* **Temperatură:** 24 - 26°C.
* **Subcultură:** Mutarea lăstarilor pe mediu proaspăt la fiecare ... zile.

---

## 🌱 4. Aclimatizarea (Deflasking)
1. **Spălarea:** Îndepărtarea totală a agarului de pe rădăcini cu apă călduță.
2. **Substrat:** Transfer în mix de [ex: Cocopeat și perlit 1:1].
3. **Umiditate:** Menținerea sub cupolă de plastic la umiditate de 90-100% în primele 2 săptămâni, apoi aerisire treptată.
```

