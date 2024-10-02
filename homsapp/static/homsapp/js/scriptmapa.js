// Inicializa o mapa
var map = L.map('map').setView([-23.55052, -46.633308], 12); // Centralizado em São Paulo

// Adiciona o tile layer (visualização do mapa)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Carrega os imóveis a partir do script JSON
var imoveis = JSON.parse(document.getElementById('imoveis_data').textContent);

// Adiciona os pontos dos imóveis
imoveis.forEach(function(imovel) {
    L.marker([imovel.latitude, imovel.longitude]).addTo(map)
        .bindPopup("Imóvel Contribuinte: " + imovel.numero_contribuinte);
});
