
  // Escuchas el evento 'submit' del formulario
  document.querySelector('form').addEventListener('submit', function(event) {
    // Previene el comportamiento por defecto del formulario
    event.preventDefault();
  
    // Calculas la suma de los valores de los checkboxes seleccionados
    var suma = Array.from(event.target.elements).reduce(function(acum, elem) {
      if (elem.type === 'checkbox' && elem.checked) {
        return acum + Number(elem.value);
      } else if (elem.type === 'text') {
        return acum + Number(elem.value);
      } else {
        return acum;
      }
    }, 0);
  
    // Envías la suma al servidor
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/ruta/a/tu/servidor');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
      if (xhr.status === 200 && xhr.responseText !== suma) {
        alert('Algo salió mal. ' + xhr.responseText);
      } else if (xhr.status !== 200) {
        alert('Hubo un error al hacer la petición. Código de estado: ' + xhr.status);
      }
    };
    xhr.send(encodeURI('suma=' + suma));
  });