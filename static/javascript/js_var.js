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


            if (blanco() == false) {
                alert("Error: Por favor no deje espacios en blanco");
            }
        };