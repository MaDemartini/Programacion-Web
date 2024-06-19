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

// API Sismologia
async function cargarSismos() {
    try {
        const response = await fetch('https://api.gael.cloud/general/public/sismos');
        const data = await response.json();
        mostrarSismos(data);
    } catch (error) {
        console.error('Error al cargar los datos de sismos:', error);
    }
  }
  
  function mostrarSismos(sismos) {
    const sismosBody = document.getElementById('sismosBody');
    sismosBody.innerHTML = '';  // Limpiar el cuerpo de la tabla
  
    sismos.forEach(sismo => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${sismo.Fecha}</td>
            <td>${sismo.Magnitud}</td>
            <td>${sismo.Profundidad}</td>
            <td>${sismo.RefGeografica}</td>
        `;
        sismosBody.appendChild(row);
    });
  }
  