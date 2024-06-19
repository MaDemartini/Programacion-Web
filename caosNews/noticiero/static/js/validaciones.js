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