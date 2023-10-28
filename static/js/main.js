document.addEventListener("DOMContentLoaded", function() {
    var fecha = new Date();
    var options = { year: 'numeric', month: 'long', day: 'numeric' };
    var fechaFormateada = fecha.toLocaleDateString("es-ES", options);
    document.getElementById("fecha").innerText = fechaFormateada;
  });

// var i = 0;
// function myFunction() {
//     var tabla = document.getElementById("miTabla");
//     var fila = tabla.insertRow(-1);
//
//     var celda1 = fila.insertCell(0);
//     var celda2 = fila.insertCell(1);
//     var celda3 = fila.insertCell(2);
//
//     celda1.innerHTML = '<img src="../../static/img/class_pollito.png" alt="Descripción de la imagen">'
//     celda2.innerHTML = "Comer";
//     celda3.innerHTML = '<input type="checkbox">';
//
//     celda1.className = "uno";
//     celda2.className = "dos";
//     celda3.className = "tres";
//
//     i++;}


function agregarFila() {
  var tabla = document.getElementById("tabla");
  var fila = tabla.insertRow(-1);

  var celda1 = fila.insertCell(0);
  var celda2 = fila.insertCell(1);
  var celda3 = fila.insertCell(2);

  var seleccion = document.getElementById("opciones").value;

  switch(seleccion) {
    case "opcion1":
      celda1.innerHTML = '<img src="../../static/img/iconoTransporte.png" alt="Descripción de la imagen">';
      celda2.innerHTML = "xd";
      celda3.innerHTML = '<input type="checkbox">';
      break;
    case "opcion2":
      celda1.innerHTML = "Opción 2 - Columna 1";
      celda2.innerHTML = "Opción 2 - Columna 2";
      celda3.innerHTML = "Opción 2 - Columna 3";
      break;
    case "opcion3":
      celda1.innerHTML = "Opción 3 - Columna 1";
      celda2.innerHTML = "Opción 3 - Columna 2";
      celda3.innerHTML = "Opción 3 - Columna 3";
      break;
    default:
      break;
   }
}