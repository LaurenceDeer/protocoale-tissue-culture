document.addEventListener("DOMContentLoaded", function() {
    const dictionary = {
        "explant": "Bucățica de plantă tăiată pentru a genera o clonă.",
        "meristem": "Țesut cu celule stem din vârfurile de creștere.",
        "calus": "Țesut amorf, nediferențiat (cicatrice/tumoare vegetală).",
        "aclimatizare": "Procesul de tranziție a plantei din borcan în mediul real.",
        "mediu ms": "Rețeta standard de nutrienți (Murashige & Skoog).",
        "agar": "Gelatina din alge folosită pentru a solidifica mediul.",
        "sucroză": "Zahăr, sursa principală de energie în vitro.",
        "pgr": "Hormon vegetal (Plant Growth Regulator).",
        "pgrs": "Hormoni vegetali (Plant Growth Regulators).",
        "auxine": "Hormoni care stimulează formarea rădăcinilor.",
        "citokinine": "Hormoni care stimulează formarea frunzelor și lăstarilor.",
        "ppm": "Biocid folosit pentru a preveni contaminarea (Plant Preservative Mixture).",
        "inocuitate": "Arta de a lucra steril, fără a introduce microbi.",
        "autoclav": "Echipament pentru sterilizare sub presiune (sau oală sub presiune).",
        "sab": "Cutie cu aer mort (Still Air Box) pentru lucrul steril.",
        "lfh": "Hotă cu flux laminar, mediu de lucru perfect steril.",
        "contaminare": "Apariția mucegaiului sau bacteriilor pe mediu.",
        "vitrificare": "Când planta devine translucidă/apoasă (hiperhidrare).",
        "fenolizare": "Când țesutul elimină compuși toxici și înnegrește mediul."
    };

    const section = document.querySelector('.main-content section');
    if (!section) return;

    const terms = Object.keys(dictionary).sort((a,b) => b.length - a.length);
    const regex = new RegExp("\\b(" + terms.join("|") + ")\\b", "gi");

    function replaceTextNodes(node) {
        if (node.nodeType === 3) {
            const text = node.nodeValue;
            if (regex.test(text)) {
                const span = document.createElement('span');
                span.innerHTML = text.replace(regex, function(match) {
                    const term = match.toLowerCase();
                    if (dictionary[term]) {
                        return `<span class="glossary-term" data-tooltip="${dictionary[term]}">${match}</span>`;
                    }
                    return match;
                });
                
                // We use replaceWith or manual replacement to not break the DOM iteration
                const frag = document.createDocumentFragment();
                Array.from(span.childNodes).forEach(child => frag.appendChild(child));
                node.parentNode.replaceChild(frag, node);
            }
        } else if (node.nodeType === 1) {
            // Ignore SCRIPT, STYLE, A tags, code blocks and headers
            const ignoreTags = ['SCRIPT', 'STYLE', 'A', 'CODE', 'PRE', 'H1', 'H2', 'H3', 'H4'];
            if (!ignoreTags.includes(node.nodeName) && !node.classList.contains('glossary-term')) {
                // Convert to array to avoid issues when replacing nodes
                const children = Array.from(node.childNodes);
                for (let i = 0; i < children.length; i++) {
                    replaceTextNodes(children[i]);
                }
            }
        }
    }

    replaceTextNodes(section);
});
