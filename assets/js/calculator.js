document.addEventListener("DOMContentLoaded", function() {
    const openBtn = document.getElementById('open-calc-btn');
    const closeBtn = document.getElementById('close-calc-btn');
    const modal = document.getElementById('calc-modal');
    
    const volInput = document.getElementById('calc-volume');
    const recipeSelect = document.getElementById('calc-recipe');
    
    const resMs = document.getElementById('res-ms');
    const resSugar = document.getElementById('res-sugar');
    const resAgar = document.getElementById('res-agar');
    const resWater = document.getElementById('res-water');

    // Recipes per 1000ml (1L)
    const recipes = {
        full: { ms: 4.43, sugar: 30, agar: 8 },
        half: { ms: 2.22, sugar: 20, agar: 7 }, // Usually less sugar and slightly softer agar is preferred for half MS depending on plant, but 20/7 is standard
        zero: { ms: 0, sugar: 30, agar: 8 }
    };

    function calculate() {
        let vol = parseFloat(volInput.value);
        if (isNaN(vol) || vol <= 0) vol = 500;
        
        const type = recipeSelect.value;
        const base = recipes[type];
        
        const ratio = vol / 1000.0;
        
        resMs.innerText = (base.ms * ratio).toFixed(2);
        resSugar.innerText = (base.sugar * ratio).toFixed(1);
        resAgar.innerText = (base.agar * ratio).toFixed(1);
        resWater.innerText = vol;

        // Visual feedback
        if(base.ms === 0) {
            resMs.innerText = "0.00";
            resMs.style.color = "#888888";
        } else {
            resMs.style.color = "var(--accent-green)";
        }
    }

    if (openBtn && modal) {
        openBtn.addEventListener('click', function(e) {
            e.preventDefault();
            modal.classList.add('active');
            calculate();
        });
    }

    if (closeBtn && modal) {
        closeBtn.addEventListener('click', function() {
            modal.classList.remove('active');
        });
    }

    // Close when clicking outside modal content
    if (modal) {
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                modal.classList.remove('active');
            }
        });
    }

    if (volInput && recipeSelect) {
        volInput.addEventListener('input', calculate);
        recipeSelect.addEventListener('change', calculate);
    }
});
