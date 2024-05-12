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

/* Header */
const header = document.querySelector("header");

const headerHTML = `
<nav class="navbar navbar-expand-lg bg-black p">
  <div class="container-fluid">
    <a class="navbar-brand" href="index.html" id="enlace-index">
      <div class="logo">
        <img src="Img/Logo.png" alt="Logo" width="120" height="120" class="d-inline-block align-text-top">
      </div>
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item bg-bordeaux">
          <a class="nav-link active text-white" href="index.html">Inicio</a>
        </li>
        <li class="nav-item bg-bordeaux">
          <a class="nav-link text-white" href="categoria.html" id="enlace-categoria">Categorías</a>
        </li>
        <li class="nav-item bg-bordeaux">
          <a class="nav-link text-white" href="contacto.html" id="enlace-enlace-contacto">Contacto</a>
        </li>
        <li class="nav-item dropdown bg-bordeaux">
          <a class="nav-link text-white dropdown-toggle" href="#unete" role="button" data-bs-toggle="dropdown" aria-expanded="false">Unete</a>
          <ul class="dropdown-menu dropdown-menu-end">
            <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">Iniciar Sesión</a></li>
            <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal2">Registrarse</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="UneNosotros.html" id="enlace-UneNosotros">Unete a Nosotros</a></li>
            <li><a class="dropdown-item" href="sobreNosotros.html" id="enlace-sobreNosotros">Quienes somos?</a></li>
          </ul>
        </li>
      </ul>
      <form class="d-flex search-form" role="search">
        <input class="input form-control me-2 search-input" type="search" placeholder="Qué buscas?" aria-label="Search">
        <button class="custom-btn btn-1 search-button" type="submit">Buscar</button>
      </form>
      <a href="#" class="text-white">
        <i class="bi bi-cart-fill fs-4"></i>
      </a>
    </div>
  </div>
</nav>

<!-- Modal Iniciar Sesión -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Iniciar Sesión</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Correo Electrónico</label>
            <input type="email" class="form-control" id="exampleInputEmail1">
          </div>
          <div class="mb-3">
            <label for="contraseña" class="form-label">Contraseña</label>
            <input type="password" class="form-control" id="contraseña" required>
          </div>
          <div class="text-center">
            <button type="submit" class="custom-btn btn-1">Iniciar Sesión</button>
          </div>
        </form>
        <hr>
        <p class="text-center">O inicia sesión con:</p>
        <div class="d-grid gap-2">
          <button class="btn btn-outline-danger" type="button">Google</button>
          <button class="btn btn-outline-primary" type="button">iCloud</button>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
      </div>
    </div>
  </div>
</div>

<!-- Modal de Registro -->
<div class="modal fade" id="exampleModal2" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Registro</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="nombre" class="form-label">Nombre</label>
            <input type="text" class="form-control" id="nombre" required>
          </div>
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Correo Electrónico</label>
            <input type="email" class="form-control" id="exampleInputEmail1">
          </div>
          <div class="mb-3">
            <label para "contraseña" class="form-label">Contraseña</label>
            <input type="password" class="form-control" required>
          </div>
          <div class="text-center">
            <button type="submit" class="custom-btn btn-1">Registrarse</button>
          </div>
        </form>
        <hr>
        <p class="text-center">O Registra con:</p>
        <div class="d-grid gap-2">
          <button class="btn btn-outline-danger" type="button">Google</button>
          <button class="btn btn-outline-primary" type="button">iCloud</button>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
      </div>
    </div>
  </div>
</div>
`;

header.innerHTML = headerHTML; // Inserta el encabezado con los modales

/* Footer */
const footer = document.querySelector("footer");

footer.innerHTML = `
  <div class="footer-container">
    <div class="footer-row">
      <div class="footer-col">
        <div class="footer-card">
          <div class="footer-icons">
            <div class="icon-container icon-instagram">
              <svg class="icon-svg instagram-svg" viewBox="0 0 16 16">
                <path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923 3.927 3.927 0 0 0-.922 1.416C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.917 3.917 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.478 2.478 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598c-.28-.28-.546-.453-.92-.599a2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 a2.667 2.667 0 0 1 0-5.334z"></path>
              </svg>
            </div>
            <div class="icon-container icon-twitter">
              <svg class="icon-svg twitter-svg" viewBox="0 0 16 16">
                <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 a3.289 3.289 0 0 0 1.018 4.382a3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 a3.283 3.283 0 0 0 3.067 2.277a6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045 a9.344 9.344 0 0 0 5.026 15z"></path>
              </svg>
            </div>
            <div class="icon-container icon-linkedin">
              <svg class="icon-svg linkedin-svg" viewBox="0 0 448 512">
                <path d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2 48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"></path>
              </svg>
            </div>
            <div class="icon-container icon-whatsapp">
              <svg class="icon-svg whatsapp-svg" viewBox="0 0 16 16">
                <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102 a7.933 7.933 0 0 0 3.79.965 h.004c4.368 0 7.926-3.558 7.93-7.93 a7.898 7.898 0 0 0-13.601 2.326z"></path>
              </svg>
            </div>
          </div>
        </div>
        <img src="Img/Logo.png" class="logofooter" alt="logofooter">      
        <p class="footer-text">SANTIAGO, CHILE FONO (562) 2 854 6300 © TODOS LOS DERECHOS RESERVADOS.</p>
      </div>
    </div>
  </div>
`;

/* Js Clima*/ 
const apiKey = '2d8aadf3fd776860d6ede68faa28b06b'; //clave de OpenWeatherMap
const cities = ['Santiago, CL', 'Viña del Mar, CL', 'Valparaíso, CL']; // Ciudades

cities.forEach((city, index) => {
    //parámetro `lang=es` para obtener los datos en español
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=es`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const cityName = data.name;
            const weatherDescription = data.weather[0].description; //Descripción en español
            const temperature = `${data.main.temp} °C`;
            const minTemp = `${data.main.temp_min} °C`;
            const maxTemp = `${data.main.temp_max} °C`;
            
            const weatherIcon = data.weather[0].icon;
            const iconUrl = `http://openweathermap.org/img/wn/${weatherIcon}@2x.png`;

            const prefix = index === 0 ? 'santiago' : (index === 1 ? 'vina' : 'valparaiso');

            document.getElementById(`city-name-${prefix}`).textContent = cityName;
            document.getElementById(`weather-description-${prefix}`).textContent = weatherDescription;
            document.getElementById(`temperature-${prefix}`).textContent = temperature;
            document.getElementById(`min-temp-${prefix}`).textContent = minTemp;
            document.getElementById(`max-temp-${prefix}`).textContent = maxTemp;
            document.getElementById(`weather-icon-${prefix}`).setAttribute("href", iconUrl);
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
            document.getElementById(`city-name-${prefix}`).textContent = 'Error';
            document.getElementById(`weather-description-${prefix}`).textContent = 'No disponible';
            document.getElementById(`temperature-${prefix}`).textContent = 'N/A';
        });
});

// Validacion js en uneNosotros.html
document.addEventListener('DOMContentLoaded', function() {
  // Obtener referencia al formulario
  const form = document.getElementById('joinForm');

  // Evento de escucha para el envío del formulario
  form.addEventListener('submit', function(event) {
      // Detener el envío del formulario
      event.preventDefault();

      // Variable para rastrear si todas las validaciones son exitosas
      let formValid = true;

      // Validar los campos del formulario
      const nombre = form.querySelector('#nombre').value.trim();
      const apellidos = form.querySelector('#apellidos').value.trim();
      const email = form.querySelector('#email').value.trim();
      const celular = form.querySelector('#celular').value.trim();
      const genero = form.querySelector('input[name="genero"]:checked');
      const fechaNacimiento = form.querySelector('#fecha-nacimiento').value.trim();
      const mensaje = form.querySelector('#mensaje').value.trim();

      // Validar que haya dos apellidos
      const apellidoArray = apellidos.split(' ');
      if (apellidoArray.length !== 2) {
          alert('Por favor ingresa dos apellidos.');
          formValid = false;
      }

      // Validar que el número de celular tenga 9 dígitos
      const celularNumber = Number(celular); // Convertir a número
      if (isNaN(celularNumber) || celular.length !== 9) {
          alert('Por favor ingresa un número de celular válido.');
          formValid = false;
      }

      // Validar que la fecha de nacimiento sea mayor de 18 años
      const fechaNacimientoDate = new Date(fechaNacimiento);
      const fechaActual = new Date();
      const edad = fechaActual.getFullYear() - fechaNacimientoDate.getFullYear();
      const mes = fechaActual.getMonth() - fechaNacimientoDate.getMonth();
      if (mes < 0 || (mes === 0 && fechaActual.getDate() < fechaNacimientoDate.getDate())) {
          edad--;
      }
      if (edad < 18) {
          alert('Debes ser mayor de 18 años para registrarte.');
          formValid = false;
      }

      // Si todas las validaciones son exitosas, enviar el formulario
      if (formValid) {
          alert('Formulario válido. Enviando solicitud...');
          form.reset(); // Reiniciar el formulario después del envío
      }
  });
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



