//Fecha actualizada
document.addEventListener("DOMContentLoaded", function() {
    var fecha = new Date();
    var options = { year: 'numeric', month: 'long', day: 'numeric' };
    var fechaFormateada = fecha.toLocaleDateString("es-ES", options);
    document.getElementById("fecha").innerText = fechaFormateada;
  });
//Barra
var numero = document.getElementById("numero").innerText;
document.getElementById("barra").value = numero;

// Selecciona la etiqueta <p> por su ID
let pTag = document.getElementById('numero');
