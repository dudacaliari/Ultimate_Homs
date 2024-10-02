document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const inputFile = document.getElementById('inputArq');
    const loadingAlert = document.getElementById('loadingAlert');
    const btnInterromper = document.getElementById('btnInterromper'); // Seleciona o botão de Interromper

    let csvProcessando = false; // Flag para controlar o estado do processamento

    if (form && inputFile && loadingAlert && btnInterromper) {
        // Evento de envio do formulário
        form.addEventListener('submit', function (event) {
            if (!inputFile.files.length) {
                alert("Por favor, selecione um arquivo CSV para carregar.");
                event.preventDefault();
                return;
            }

            // Exibe a mensagem de carregamento e define a flag
            loadingAlert.classList.remove('hidden');
            loadingAlert.classList.add('visible');
            csvProcessando = true;
        });

        // Evento para o botão de Interromper
        btnInterromper.addEventListener('click', function () {
            if (csvProcessando) {
                // Cancela o envio do formulário e oculta a mensagem de carregamento
                csvProcessando = false;
                loadingAlert.classList.remove('visible');
                loadingAlert.classList.add('hidden');

                // Limpa o campo de upload para reiniciar o processo
                inputFile.value = '';
                alert("Processamento interrompido. Você pode carregar um novo arquivo.");
            }
        });
    }
});
