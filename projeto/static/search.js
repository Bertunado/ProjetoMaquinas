document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("searchInput");
    const suggestionsBox = document.getElementById("suggestions");

    input.addEventListener("input", function () {
        const query = input.value.trim().toLowerCase();
        suggestionsBox.innerHTML = "";

        if (query.length === 0) {
            suggestionsBox.style.display = "none";
            return;
        }

        // links para o usuario comum sem login especial
        const suggestions = [
            { name: "Omera 1 - Prensas Fábrica 2", url: "/omera1_prensas-fabrica2/" },
            { name: "Omera 2 - Prensas Fábrica 2", url: "/omera2_prensas-fabrica2/" },
            { name: "Omera 3 - Prensas Fábrica 2", url: "/omera3_prensas-fabrica2/" },
            { name: "Omera 4 - Prensas Fábrica 2", url: "/omera4_prensas-fabrica2/" },
            { name: "Pintura pó 3 - Pintura Fábrica 2", url: "/pinturapo3_F2/" },
            { name: "Pintura pó 4 - Pintura Fábrica 2", url: "/pinturapo4_F2/" },
            { name: "Pintura Líquida - Pintura Fábrica 3", url: "/pinturaliquidaF3/" },
            { name: "Sares 1 - Perfiladoras Fábrica 2", url: "/sares1_perfiladoras-fabrica2/" },
            { name: "Sares 2 - Perfiladoras Fábrica 2", url: "/sares2_perfiladoras-fabrica2/" },
            { name: "Sares 3 - Perfiladoras Fábrica 3", url: "/sares3_perfiladorasF3/" },
            { name: "Sares 4 - Perfiladoras Fábrica 3", url: "/sares4_perfiladorasF3" },
            { name: "Cosma - Perfiladoras Fábrica 2", url: "/cosma_perfiladoras-fabrica2/" },
            { name: "Fagor Gabinete - Perfiladoras Fábrica 2", url: "/fagorGabinete-perfiladoras-fabrica2/" },
            { name: "Olma FH - Perfiladoras Fábrica 2", url: "/olmaFH_perfiladoras-fabrica2" },
            { name: "Jundiai - Perfiladoras Fábrica 3", url: "/jundiai_perfiladorasF3" },
            { name: "Aida - Prensa Fábrica 3", url: "/Aita_prensa-F3/" },
            { name: "Fagor - Prensas Fábrica 3", url: "/fagor_prensa-F3/" },
        ];

        const filtered = suggestions.filter(item =>
            item.name.toLowerCase().includes(query)
        );

        if (filtered.length === 0) {
            suggestionsBox.style.display = "none";
            return;
        }

        filtered.forEach(item => {
            const div = document.createElement("div");
            div.classList.add("suggestion-item");
            div.textContent = item.name;
            div.addEventListener("click", function () {
                window.location.href = item.url; // ✅ Redireciona para URL pública correta
            });
            suggestionsBox.appendChild(div);
        });

        suggestionsBox.style.display = "block";
    });

    // Esconde as sugestões ao clicar fora
    document.addEventListener("click", function (event) {
        if (!suggestionsBox.contains(event.target) && event.target !== input) {
            suggestionsBox.style.display = "none";
        }
    });
});