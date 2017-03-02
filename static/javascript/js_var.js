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

function validar() {

        var txtCorreo = document.getElementById('email').value;
        var txtDocumento = document.getElementById('documento').value;
        var cmbSelector = document.getElementById('id_curso').value;
        var cmbSelectorGrupo = document.getElementById('id_grupo').value;
        var rdbGenero = document.getElementById('genero').value;

        var banderaRBTN = false;
        for(var i = 0; i < rdbGenero.length; i++){
            if(rdbGenero[i].checked){
                banderaRBTN = true;
                break;
            }
        }
debugger;
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
        }else if (!/^([0-9])*$/.test(txtDocumento)){ //Test campo obligatorio
            var src = "<strong>ERROR: El campo documento debe ser solo números y no debe contener espacios.</strong> <br>";
            $("#errors").html(src);
            document.getElementById("errors").style.display="block";
            return false;
        }else if(!banderaRBTN){ //Test checkBox
            var src = "<strong>ERROR: Debe seleccionar un Género</strong> <br>";
            $("#errors").html(src);
            document.getElementById("errors").style.display="block";
            return false;
        }else if(cmbSelector == null || cmbSelector == 0){
            var src = "<strong>ERROR: Debe seleccionar un curso</strong> <br>";
            $("#errors").html(src);
            document.getElementById("errors").style.display="block";
            return false;
        }else if(cmbSelectorGrupo == null || cmbSelectorGrupo == 0){
            var src = "<strong>ERROR: Debe seleccionar un grupo</strong> <br>";
            $("#errors").html(src);
            document.getElementById("errors").style.display="block";
            return false;
        }else {
            return true;
        }
};