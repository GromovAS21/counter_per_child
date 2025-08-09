const genderSocket = new WebSocket(
    'wss://' + window.location.host + '/ws/gender-updates/'
);

// Функция для обновления подсветки карточек
function updateLeadingCard() {
    const girlTotal = parseInt(document.getElementById('girlCardTotal').textContent) || 0;
    const boyTotal = parseInt(document.getElementById('boyCardTotal').textContent) || 0;
    const girlCard = document.getElementById('girlCard');
    const boyCard = document.getElementById('boyCard');

    // Убираем подсветку и пульсацию с обеих карточек
    girlCard.classList.remove('leading-card', 'pulsing-card');
    boyCard.classList.remove('leading-card', 'pulsing-card');

    // Добавляем эффекты к карточке с большей суммой
    if (girlTotal > boyTotal) {
        girlCard.classList.add('leading-card', 'pulsing-card');
    } else if (boyTotal > girlTotal) {
        boyCard.classList.add('leading-card', 'pulsing-card');
    }
}

// Обработка сообщений WebSocket
genderSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const isBoy = data.gender === "Мальчик";
    const totalElementId = isBoy ? 'boyCardTotal' : 'girlCardTotal';
    const cardId = isBoy ? 'boyCard' : 'girlCard';
    const currentValue = parseInt(document.getElementById(totalElementId).textContent) || 0;
    const isIncrease = data.amount > currentValue;

    // Анимация изменения числа
    animateNumberChange(totalElementId, data.amount, isIncrease, function() {
        // Обновляем лидирующую карточку
        updateLeadingCard();

        // Кратковременная пульсация обновленной карточки
        const card = document.getElementById(cardId);
        card.classList.add('updated-pulse');
        setTimeout(() => {
            card.classList.remove('updated-pulse');
        }, 500);
    });
};

// Функция анимации числа с цветом
function animateNumberChange(elementId, newValue, isIncrease, callback) {
    const element = document.getElementById(elementId);
    const startValue = parseInt(element.textContent) || 0;
    const duration = 500;
    const startTime = performance.now();

    // Устанавливаем цвет в зависимости от изменения
    element.classList.add(isIncrease ? 'increasing' : 'decreasing');

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const currentValue = Math.floor(startValue + (newValue - startValue) * progress);

        element.textContent = currentValue;

        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            // Убираем классы цвета через небольшой промежуток времени
            setTimeout(() => {
                element.classList.remove('increasing', 'decreasing');
                if (callback) callback();
            }, 300);
        }
    }

    requestAnimationFrame(update);
}

// Инициализация при загрузке
document.addEventListener('DOMContentLoaded', function() {
    updateLeadingCard();
});

// Обработка закрытия соединения
genderSocket.onclose = function(e) {
    console.error('WebSocket closed:', e);
    setTimeout(() => {
        window.location.reload();
    }, 5000);
};