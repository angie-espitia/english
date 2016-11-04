function eliminarestudiante(estudianteId) {
        var request = $.ajax({
            type: "POST",
            url: "{% url 'eliminar_estudiante' %}",
            data: {
                "csrfmiddlewaretoken": "{{ csrf_token }}",
                "estudiante_id": estudianteId                    
            },
        });
        request.done(function(response) {
            alert("Estudiante eliminado");
            // Cierra el modal, oculta el identificador eliminado, etc.
        });
    }