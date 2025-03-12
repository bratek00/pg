const apiKey = 'ceb7c9609bc251b37fda2d9ccad58d05'; // Získejte bezplatný API klíč z openweathermap.org

async function getWeather() {
    const city = document.getElementById('cityInput').value;
    if (!city) {
        alert('Prosím, zadejte město!');
        return;
    }

    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=cz`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Město nenalezeno');
        }
        const data = await response.json();
        displayWeather(data);
    } catch (error) {
        document.getElementById('weatherResult').innerHTML = `<p class="text-danger">${error.message}</p>`;
    }
}

function displayWeather(data) {
    console.log("my data "+JSON.stringify(data,null,2));
    const { name, main, weather, wind } = data;
    const myDataInput =+JSON.stringify(data,null,2);
    const weatherHtml = `
        <h3>${name}</h3>
        <p><strong>Teplota:</strong> ${main.temp}°C</p>
        <p><strong>Pocitová teplota:</strong> ${main.feels_like}°C</p>
        <p><strong>Počasí:</strong> ${weather[0].description}</p>
        <p><strong>Pressure:</strong> ${main.pressure}</p>
        <p><strong>Rychlost vetra:</strong> ${wind.speed}</p>
        <img src="https://openweathermap.org/img/wn/${weather[0].icon}@2x.png" alt="Ikona počasí">
        <hr>
    `;

    document.getElementById('weatherResult').innerHTML = weatherHtml;
}
