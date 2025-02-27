$(document).ready(function() {
    $('#id_responsavel').autocomplete({
        source: function(request, response) {
            $.ajax({
                url: '{% url "formulario:buscar_responsavel" %}', 
                data: {
                    'q': request.term  
                },
                success: function(data) {
                    response($.map(data.results, function(item) {
                        return {
                            label: item.nome_responsavel,  
                            value: item.id_responsavel    
                        };
                    }));
                }
            });
        },
        minLength: 2,  
        select: function(event, ui) {
            $('#id_responsavel').val(ui.item.label);
            $('#responsavel_id').val(ui.item.value); 
            return false;  
        }
    });
});