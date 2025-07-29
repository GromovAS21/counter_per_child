const genderSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/gender-updates/'
);

// Функция для обновления подсветки карточек
function updateLeadingCard() {
    const girlTotal = parseInt(document.getElementById('girlCardTotal').textContent) || 0;
    const boyTotal = parseInt(document.getElementById('boyCardTotal').textContent) || 0;
    const girlCard = document.getElementById('girlCard');
    const boyCard = document.getElementById('boyCard');

    // Убираем подсветку с обеих карточек
    girlCard.classList.remove('leading-card');
    boyCard.classList.remove('leading-card');

    // Добавляем подсветку к карточке с большей суммой
    if (girlTotal > boyTotal) {
        girlCard.classList.add('leading-card');
    } else if (boyTotal > girlTotal) {
        boyCard.classList.add('leading-card');
    }
}

// Обработка сообщений WebSocket
genderSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const isBoy = data.name === "Мальчик";
    const totalElementId = isBoy ? 'boyCardTotal' : 'girlCardTotal';
    const cardId = isBoy ? 'boyCard' : 'girlCard';

    // Анимация изменения числа
    animateNumberChange(totalElementId, data.total, function() {
        // После завершения анимации обновляем подсветку
        updateLeadingCard();

        // Добавляем эффект пульсации к обновленной карточке
        const card = document.getElementById(cardId);
        card.classList.add('updated-pulse');
        setTimeout(() => {
            card.classList.remove('updated-pulse');
        }, 1000);
    });
};

// Функция анимации числа
function animateNumberChange(elementId, newValue, callback) {
    const element = document.getElementById(elementId);
    const startValue = parseInt(element.textContent) || 0;
    const duration = 500;
    const startTime = performance.now();

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const currentValue = Math.floor(startValue + (newValue - startValue) * progress);

        element.textContent = currentValue;

        if (progress < 1) {
            requestAnimationFrame(update);
        } else if (callback) {
            callback();
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