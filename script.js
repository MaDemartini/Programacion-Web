const header = document.querySelector("header");

const headerHTML = `
<nav class="navbar navbar-expand-lg bg-black p">
  <div class="container-fluid">
    <a class="navbar-brand" href="index.html">
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
          <a class="nav-link text-white" href="categoria.html">Categorías</a>
        </li>
        <li class="nav-item bg-bordeaux">
          <a class="nav-link text-white" href="contacto.html">Contacto</a>
        </li>
        <li class="nav-item dropdown bg-bordeaux">
          <a class="nav-link text-white dropdown-toggle" href="#unete" role="button" data-bs-toggle="dropdown" aria-expanded="false">Unete</a>
          <ul class="dropdown-menu dropdown-menu-end">
            <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">Iniciar Sesión</a></li>
            <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal2">Registrarse</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="UneNosotros.html">Unete a Nosotros</a></li>
          </ul>
        </li>
      </ul>
      <form class="d-flex search-form" role="search">
        <input class="form-control me-2 search-input" type="search" placeholder="Buscar" aria-label="Search">
        <button class="btn btn-outline-light search-button" type="submit">Buscar</button>
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
            <button type="submit" class="btn btn-primary">Iniciar Sesión</button>
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
            <button type="submit" class="btn btn-primary">Registrarse</button>
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


const footer = document.querySelector("footer");

footer.innerHTML = `
  <div class="container">
    <div class="row">
      <div class="col">
        <p class="text-center">SANTIAGO, CHILE FONO (562) 2 854 6300 © TODOS LOS DERECHOS RESERVADOS.</p>
      </div>
    </div>
  </div>
`;
