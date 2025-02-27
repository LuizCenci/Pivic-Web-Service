document.addEventListener('DOMContentLoaded', function () {
    const cepInput = document.getElementById('id_cep');
    const cidadeInput = document.getElementById('id_cidade');
    const estadoInput = document.getElementById('id_estado');
    const paisInput = document.getElementById('id_pais');
    
    // Desabilitar campos de cidade, estado e país
    cidadeInput.setAttribute('readonly', true);
    estadoInput.setAttribute('readonly', true);
    paisInput.setAttribute('readonly', true); 

    cepInput.addEventListener('blur', function () {
        let cep = cepInput.value.replace(/\D/g, ''); // Remove caracteres não numéricos
        if (cep.length === 8) {
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(response => response.json())
                .then(data => {
                    if (data.erro) {
                        alert('CEP não encontrado!');
                        // Limpar os campos caso o CEP não seja válido
                        cidadeInput.value = '';
                        estadoInput.value = '';
                        paisInput.value = '';  // Limpar o país também
                    } else {
                        cidadeInput.value = data.localidade;
                        estadoInput.value = data.uf;
                        paisInput.value = 'Brasil';
                    }
                })
                .catch(error => alert('Erro ao buscar CEP.'));
        }
    });

    // Limpar os campos de cidade, estado e país quando o usuário apagar o CEP
    cepInput.addEventListener('input', function () {
        cidadeInput.value = '';
        estadoInput.value = '';
        paisInput.value = '';  
    });
})