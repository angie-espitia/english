function blanco() {
        validaformulario = document.formularioregistro;

        for (var i=0; i< validaformulario.length; i++) {

            if(validaformulario[i].type == "text" || validaformulario[i].type == "number" || validaformulario[i].type == "date") {

                if (validaformulario[i].value.length == 0 || /^\s*$/.test(validaformulario[i].value)){
                    
                    return false;
                }       
            }
        }
        return true;
};

function radio() {

    opciones = document.getElementsByName("sexo");
    var seleccionado = false;
    for(var i=0; i<opciones.length; i++) {    
        if(opciones[i].checked) {
        seleccionado = true;
        break;
        }
    }

        if(!seleccionado) {
        return false;
        }
};

function select(){
    indice = document.getElementById("id_grupo").selectedIndex;
        if( indice == null || indice == 0 ) {
          return false;
        }
};

function vacio() {
    txtUsuario = document.getElementById('usuario').value;
    for ( i = 0; i < txtUsuario.length; i++ ) {
        if ( txtUsuario.charAt(i) != " " ) {
        return true
        }
    }
    return false
};

function validar() {

        var txtCorreo = document.getElementById('email').value;
        var txtDocumento = document.getElementById('documento').value;
        var cmbSelector = document.getElementById('id_curso').value;

        if (blanco() == false) {
            var src = "<strong>ERROR: No deben haber campos vacios.</strong> <br>";
            $("#errors").html(src);
            document.getElementById("errors").style.display="block";
            return false;            
        }else if(!(/\S+@\S+\.\S+/.test(txtCorreo))){ //Test correo
            var src = "<strong>ERROR: Debe escribir un correo válido</strong> <br>";
            $("#errors").html(src);
            document.getElementById("errors").style.display="block";
            return false;
        }else if (vacio() == false){ //Test campo obligatorio
            var src = "<strong>ERROR: El campo Username no debe contener espacios en blanco.</strong> <br>";
            $("#errors").html(src);
            document.getElementById("errors").style.display="block";
            return false;
        }else if (!/^([0-9])*$/.test(txtDocumento)){ //Test campo obligatorio
            var src = "<strong>ERROR: El campo documento debe ser solo números y no debe contener espacios.</strong> <br>";
            $("#errors").html(src);
            document.getElementById("errors").style.display="block";
            return false;
        }else if(radio() == false){ //Test checkBox
            var src = "<strong>ERROR: Debe seleccionar un Género</strong> <br>";
            $("#errors").html(src);
            document.getElementById("errors").style.display="block";
            return false;
        }else if(cmbSelector == null || cmbSelector == 0){
            var src = "<strong>ERROR: Debe seleccionar un curso</strong> <br>";
            $("#errors").html(src);
            document.getElementById("errors").style.display="block";
            return false;
        }else if(select() == false){
            var src = "<strong>ERROR: Debe seleccionar un grupo</strong> <br>";
            $("#errors").html(src);
            document.getElementById("errors").style.display="block";
            return false;
        }else {
            return true;
            location.reload();
        }
};
