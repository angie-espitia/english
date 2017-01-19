
var lista = ["BELIEVE","DRIVE","ENJOY","JUMP","REMIND","REMEMBER","SCREAM","SPEAK","SUFFER","SWIM","TEACH","THROW","THINK","UNDERSTAND","WALK","WATCH","WAER","WISH","WORK","WRITE"];
var fallos = 0;
nuevo();
imgahorcado(0);
document.getElementById("palabra").value = lineas.join(" ");

function nuevo(){

   random=Math.round(Math.random() * (lista.length-1));
   arreglo = lista[random];
   palabra = arreglo.split("");
   lineas = juegonuevo(palabra.length);
   fallos = 0;
   console.log(random);
   console.log(lineas);
   borrarAhorcado();
   imgahorcado(0);
   tecladoon();
   document.getElementById("palabra").value = lineas.join(" ");
   document.getElementById("ganastes").style.display="none";
   document.getElementById("perdistes").style.display="none";

}

function tecladoon(){

	document.getElementById("A").disabled = false;
	document.getElementById("B").disabled = false;
	document.getElementById("C").disabled = false;
	document.getElementById("D").disabled = false;
	document.getElementById("E").disabled = false;
	document.getElementById("F").disabled = false;
	document.getElementById("G").disabled = false;
	document.getElementById("H").disabled = false;
	document.getElementById("I").disabled = false;
	document.getElementById("J").disabled = false;
	document.getElementById("K").disabled = false;
	document.getElementById("L").disabled = false;
	document.getElementById("M").disabled = false;
	document.getElementById("N").disabled = false;
	document.getElementById('Ñ').disabled = false;
	document.getElementById("O").disabled = false;
	document.getElementById("P").disabled = false;
	document.getElementById("Q").disabled = false;
	document.getElementById("R").disabled = false;
	document.getElementById("S").disabled = false;
	document.getElementById("T").disabled = false;
	document.getElementById("U").disabled = false;
	document.getElementById("V").disabled = false;
	document.getElementById("W").disabled = false;
	document.getElementById("X").disabled = false;
	document.getElementById("Y").disabled = false;
	document.getElementById("Z").disabled = false;

}

function tecladooff(){

	document.getElementById("A").disabled = true;
	document.getElementById("B").disabled = true;
	document.getElementById("C").disabled = true;
	document.getElementById("D").disabled = true;
	document.getElementById("E").disabled = true;
	document.getElementById("F").disabled = true;
	document.getElementById("G").disabled = true;
	document.getElementById("H").disabled = true;
	document.getElementById("I").disabled = true;
	document.getElementById("J").disabled = true;
	document.getElementById("K").disabled = true;
	document.getElementById("L").disabled = true;
	document.getElementById("M").disabled = true;
	document.getElementById("N").disabled = true;
	document.getElementById('Ñ').disabled = true;
	document.getElementById("O").disabled = true;
	document.getElementById("P").disabled = true;
	document.getElementById("Q").disabled = true;
	document.getElementById("R").disabled = true;
	document.getElementById("S").disabled = true;
	document.getElementById("T").disabled = true;
	document.getElementById("U").disabled = true;
	document.getElementById("V").disabled = true;
	document.getElementById("W").disabled = true;
	document.getElementById("X").disabled = true;
	document.getElementById("Y").disabled = true;
	document.getElementById("Z").disabled = true;

}

function comparar(acierto){

	this.acierto = acierto;
	document.getElementById(acierto).disabled = true;

}

comparar.prototype.acertar = function(lineas) {

	palabra = lista[random].split("");

	if(palabra.indexOf(this.acierto) != -1){

		console.log(this.acierto+" Si Esta");

		for (var i = 0; i <= palabra.length; i++) {

			if(palabra[i] == this.acierto){

				lineas[i] = this.acierto;

			}

		};

	}else{

		console.log(this.acierto+" No Esta");
		fallos++;
		imgahorcado(fallos);

	}
		console.log(lineas);
		document.getElementById("palabra").value = lineas.join(" ");

		if(lineas.join() == palabra.join()){

         document.getElementById("ganastes").style.display="inline";
			tecladooff();

		}

		if(fallos == 6){

         document.getElementById("perdistes").style.display="inline"; 
         tecladooff();
			// location.reload();

		}		
};

function reFresh() {

   location.reload(true)
 
}

function principal(acierto){

	this.acierto = acierto;
	obj = new comparar(this.acierto);
	obj.acertar(lineas);

}

function juegonuevo(palabra){

	this.palabra = palabra;
	var line = new Array();

		for (var i = 1; i <= this.palabra; i++) {

			line.push("_");

		};

	return line;

}

function cargaContextoCanvas(idCanvas){

   var elemento = document.getElementById(idCanvas);

   if(elemento && elemento.getContext){

      var contexto = elemento.getContext('2d');

      if(contexto){

         return contexto;

      }

   }

   return false;

}

function borrarAhorcado(){

   var oCanvas = document.getElementById("ahorcado");
   var oContext = oCanvas.getContext("2d");
 
   oCanvas.width = oCanvas.width;

}

function horca(ctx){

   ctx.fillStyle = '#9d3d10';
   ctx.fillRect(64,9,26,237);
   ctx.fillRect(175,193,26,53);
   ctx.fillRect(64,193,136,15);
   ctx.fillRect(64,9,115,11);
   ctx.fillRect(170,10,10,60);

   ctx.beginPath();
   ctx.moveTo(64,65);
   ctx.lineTo(64,80);
   ctx.lineTo(133,11);
   ctx.lineTo(118,11);
   ctx.fill();

}

function cabeza(ctx){

   ctx.beginPath();
	
	ctx.moveTo(40,70);
   	ctx.arc(175,60,30,0,(Math.PI/180)*360,true);
    ctx.fillStyle = '#011dd0';
    ctx.lineWidth = 10;
    ctx.fill();
    
}

function cuerpo(ctx){

   ctx.beginPath();
   ctx.moveTo(171,82);
   ctx.lineTo(168,119);
   ctx.lineTo(162,147);
   ctx.lineTo(189,149);
   ctx.lineTo(185,111);
   ctx.lineTo(183,83);
   ctx.fill()

}

function brazizq(ctx){

   ctx.beginPath();
   ctx.moveTo(173,102);
   ctx.lineTo(140,128);
   ctx.lineTo(155,133);
   ctx.lineTo(178,114);
   ctx.fill()

}

function brazoder(ctx){

   ctx.beginPath();
   ctx.moveTo(180,99);
   ctx.lineTo(222,121);
   ctx.lineTo(209,133);
   ctx.lineTo(183,110);
   ctx.fill()

}

function pierizq(ctx){

   ctx.beginPath();
   ctx.moveTo(166,142);
   ctx.lineTo(139,175);
   ctx.lineTo(164,178);
   ctx.lineTo(175,144);
   ctx.fill()

}
function pierder(ctx){

   ctx.beginPath();
   ctx.moveTo(178,145);
   ctx.lineTo(193,178);
   ctx.lineTo(212,170);
   ctx.lineTo(188,142);
   ctx.fill()

}

function imgahorcado(numerrores){

   var contexto = cargaContextoCanvas('ahorcado');

   if(contexto){

      horca(contexto);

      if(fallos>0){

         cabeza(contexto)

      }

      contexto.fillStyle = '#011dd0';

      if(fallos>1){

         cuerpo(contexto)

      }

      if(fallos>2){

         brazizq(contexto)

      }

      if(fallos>3){

         brazoder(contexto)

      }

      if(fallos>4){

         pierizq(contexto)

      }

      if(fallos>5){

         pierder(contexto)

      }
      
   }

}