$(document).ready(function() {
    $('#id_responsavel').autocomplete({
        source: function(request, response) {
            $.ajax({
                url: '{% url "formulario:buscar_responsavel" %}', 
                data: {
                    'q': request.term  // Envia o termo digitado para o backend
                },
                success: function(data) {
                    // Mapeia os resultados para o formato esperado pelo autocomplete
                    response($.map(data.results, function(item) {
                        return {
                            label: item.nome_responsavel,  // Texto exibido na sugestão
                            value: item.id_responsavel    // Valor associado ao item
                        };
                    }));
                }
            });
        },
        minLength: 2,  // Só faz a busca após 2 caracteres
        select: function(event, ui) {
            // Quando um item é selecionado, preenche o campo com o nome do responsável
            $('#id_responsavel').val(ui.item.label);
            return false;  // Impede que o valor padrão (ID) seja inserido no campo
        }
    });
});