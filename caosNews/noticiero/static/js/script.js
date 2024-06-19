/* Modal Bienvenida Usuario */ 
document.addEventListener('DOMContentLoaded', function() {
  // Comprobar si el modal ya se mostró
  var modalShown = sessionStorage.getItem('modalShown');

  if (!modalShown) {
      var myModal = new bootstrap.Modal(document.getElementById('welcomeModal'));
      myModal.show();

      // Marcar que el modal ya se mostró para no mostrarlo de nuevo
      sessionStorage.setItem('modalShown', 'true');
  }
});


// Cuando se hace clic en un enlace para ir a categoria.html
document.getElementById('enlace-categoria').addEventListener('click', function(event) {
  // Previene la acción por defecto del enlace
  event.preventDefault();

  // Muestra el loader
  document.querySelector('.loader').style.display = 'block';

  // Simula un retraso antes de redireccionar (por ejemplo, 1 segundo)
  setTimeout(function() {
    // Redirecciona a categoria.html
    window.location.href = 'categoria.html';
  }, 1000); // 1000 milisegundos = 1 segundo

  return false;
});



