// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla = "#tabla_estudiante"; // id
var nombre_boton_eliminar = ".delete"; // Clase
var nombre_formulario_modal = "#frmEliminar"; //id
var nombre_ventana_modal = "#myModal"; // id
// Fin de configuraciones

$(window).ready(function() {
    $(document).on('ready', function () {
        $(nombre_boton_eliminar).on('click', function (e) {
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idEstudiante').val(Pid);
            $('#modal_name').text(name);
        });

        var options = {
            success: function (response) {
                if (response.status == "True") {
                    alert("Eliminado!");
                    var idProd = response.estudiante_id;
                    var elementos = $(nombre_tabla + '  >tr').length;
                    if (elementos == 1) {
                        location.reload();
                    } else {
                        $('#tr' + idProd).remove();
                        $(nombre_ventana_modal).modal('hide');
                    }

                } else {
                    alert("Hubo un error al eliminar!");
                    $(nombre_ventana_modal).modal('hide');
                }
            }
        };

        $(nombre_formulario_modal).ajaxForm(options);
    });
}); 