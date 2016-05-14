
$(window).ready(function(){
    $("#b").click(function() {
        consulta = $("#b").val();
        $.ajax({
             data: {'username': consulta},
             url: '/buscar_estudiante/',
             type: 'get',

             success : function(data) {
                    var nombre = data.nombre;
                    var apellido = data.apellido;
                    $("#first_name").val(nombre);
                    $("#last_name").val(apellido);
                    $("#nombre").text(data.nombre + ' ' + data.apellido);
             },
             error : function(message) {
                     var error = "Error";
                     $("#nombre").text(error);
      }
         });
    });
});