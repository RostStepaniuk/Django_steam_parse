// Загрузка данных с помощью JavaScript
fetch('{% url "allgames" %}')
    .then(response => response.json())
    .then(data => {
        // Вывод данных на странице
        const gamesContainer = document.getElementById('games-container');
        data.games.forEach(game => {
            const gameElement = document.createElement('li');
            gameElement.innerHTML = `
                <strong>${game.title}</strong><br>
                Original Price: ${game.price}<br>
                Discounted Price: ${game.disc_price}
            `;
            gamesContainer.appendChild(gameElement);
        });
    })
    .catch(error => console.error('Произошла ошибка при загрузке данных: ', error));