// links para a pagina do superusuario logado

document.addEventListener('DOMContentLoaded', function () {
    const items = [
        { name: "Omera 1", slug: "omera1_prensas_fabrica2" },
        { name: "Omera 2", slug: "omera2_prensas_fabrica2" },
        { name: "Omera 3", slug: "omera3_prensas_fabrica2" },
        { name: "Omera 4", slug: "omera4_prensas_fabrica2" },
        { name: "Pintura pó 3", slug: "pinturapo3_F2" },
        { name: "Pintura pó 4", slug: "pinturapo4_F2" },
        { name: "Cosma", slug: "cosma_perfiladoras_fabrica2" },
        { name: "Fagor", slug: "fagor_prensa_F3" },
        { name: "Fagor Gabinetes", slug: "fagorGabinete_perfiladoras_fabrica2" },
        { name: "Jundiai", slug: "jundiai_perfiladorasF3" },
        { name: "Olma FH", slug: "olmaFH_perfiladoras_fabrica2" },
        { name: "Pintura Líquida", slug: "pinturaliquidaF3" },
        { name: "Sares 1", slug: "sares1_perfiladoras_fabrica2" },
        { name: "Sares 2", slug: "sares2_perfiladoras_fabrica2" },
        { name: "Sares 3", slug: "sares3_perfiladoraF3" },
        { name: "Sares 4", slug: "sares4_perfiladorasF3" },
        { name: "Aida", slug: "Aita_prensa_F3" }
    ];

    const searchInput = document.getElementById('searchInput');
    const suggestionsBox = document.getElementById('suggestions');

    if (!searchInput || !suggestionsBox) {
        console.error('Elemento de busca não encontrado!');
        return;
    }

    searchInput.addEventListener('input', function () {
        const input = searchInput.value.toLowerCase().trim();
        suggestionsBox.innerHTML = '';

        if (input === '') {
            suggestionsBox.style.display = 'none';
            return;
        }

        const filteredItems = items.filter(item =>
            item.name.toLowerCase().includes(input)
        );

        if (filteredItems.length === 0) {
            suggestionsBox.style.display = 'none';
            return;
        }

        filteredItems.forEach(item => {
            const suggestionItem = document.createElement('div');
            suggestionItem.textContent = item.name;
            suggestionItem.classList.add('suggestion-item');

            suggestionItem.addEventListener('click', () => {
                // Redireciona para a URL Django
                window.location.href = `/adicionar-peca/${item.slug}/`;
            });

            suggestionsBox.appendChild(suggestionItem);
        });

        suggestionsBox.style.display = 'block';
    });

    // Oculta sugestões ao clicar fora
    document.addEventListener('click', function (e) {
        if (!searchInput.contains(e.target) && !suggestionsBox.contains(e.target)) {
            suggestionsBox.style.display = 'none';
        }
    });
});