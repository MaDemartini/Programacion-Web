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



// Loader
document.addEventListener("DOMContentLoaded", function() {
  // Mostrar el loader al cargar la página
  var loader = document.querySelector('.loader');
  loader.style.display = 'block';

  // Deshabilitar el scroll del body
  document.body.classList.add('body-scroll-disabled');

  // Simulación de carga (ejemplo: ocultar después de 2 segundos)
  setTimeout(function() {
    loader.style.display = 'none';
    document.getElementById('main-content').style.display = 'block';

    // Habilitar el scroll del body nuevamente
    document.body.classList.remove('body-scroll-disabled');
  }, 2000);
});




