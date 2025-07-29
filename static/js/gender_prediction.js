// WebSocket соединение
const socket = new WebSocket(
    'ws://' + window.location.host + '/ws/updates/'
);

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    // Обновляем данные на странице
    document.getElementById('girlCardTotal').innerText = data.data[1].total;
    document.getElementById('boyCardTotal').innerText = data.data[0].total;

    // Обновляем подсветку карточек
    highlightCardWithHigherTotal();
};

socket.onclose = function(e) {
    console.error('WebSocket closed unexpectedly');
};

// Создаем плавающие элементы для фона
function createFloatingElements() {
    const colors = [
        // Розовые оттенки (для девочки)
        'rgba(255, 105, 180, 0.6)', // Ярко-розовый
        'rgba(255, 182, 193, 0.6)', // Светло-розовый
        'rgba(219, 112, 147, 0.6)', // Розово-фиолетовый
        'rgba(255, 192, 203, 0.6)', // Розовый

        // Голубые оттенки (для мальчика)
        'rgba(100, 181, 246, 0.6)', // Светло-голубой
        'rgba(66, 165, 245, 0.6)',  // Голубой
        'rgba(30, 136, 229, 0.6)',  // Ярко-голубой
        'rgba(144, 202, 249, 0.6)'  // Бледно-голубой
    ];

    const container = document.getElementById('floating-elements');
    const shapes = [
        'polygon(50% 0%, 0% 100%, 100% 100%)', // Треугольник (лепесток)
        'polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)', // Ромб
        'polygon(50% 0%, 100% 38%, 82% 100%, 18% 100%, 0% 38%)', // 5-угольник (цветок)
        'circle(50% at 50% 50%)', // Круг (капелька)
        'ellipse(25% 40% at 50% 50%)' // Овал (листик)
    ];

    for (let i = 0; i < 50; i++) {
        const element = document.createElement('div');
        element.className = 'floating-element';

        // Случайные параметры
        const size = Math.random() * 30 + 10;
        const duration = Math.random() * 25 + 15;
        const delay = Math.random() * 20;
        const xOffset = Math.random() * 2 - 1;
        const rotation = Math.random() * 720 - 360;
        const color = colors[Math.floor(Math.random() * colors.length)];
        const shapeType = shapes[Math.floor(Math.random() * shapes.length)];

        element.style.width = `${size}px`;
        element.style.height = `${size * (Math.random() * 0.5 + 0.8)}px`;
        element.style.left = `${Math.random() * 100}vw`;
        element.style.animationDuration = `${duration}s`;
        element.style.animationDelay = `${delay}s`;
        element.style.setProperty('--x-offset', xOffset);
        element.style.backgroundColor = color;
        element.style.clipPath = shapeType;
        element.style.transform = `rotate(${rotation}deg)`;

        // Добавляем немного вариативности
        if (color.includes('181, 246') || color.includes('165, 245')) {
            // Для голубых элементов чаще делаем круглую форму
            element.style.borderRadius = Math.random() > 0.3 ? '50%' : '0';
        } else {
            // Для розовых элементов делаем более острые формы
            element.style.borderRadius = Math.random() > 0.8 ? '50%' : '0';
        }

        container.appendChild(element);
    }
}

// Функция для сравнения значений total и добавления анимации
function highlightCardWithHigherTotal() {
    const girlCard = document.getElementById('girlCard');
    const boyCard = document.getElementById('boyCard');

    // Удаляем подсветку с обеих карточек
    girlCard.classList.remove('highlight-card');
    boyCard.classList.remove('highlight-card');

    // Получаем текущие значения
    const girlCardTotal = parseFloat(document.getElementById('girlCardTotal').innerText.replace(/[^0-9.-]/g, ''));
    const boyCardTotal = parseFloat(document.getElementById('boyCardTotal').innerText.replace(/[^0-9.-]/g, ''));

    // Добавляем подсветку к карточке с большим значением
    if (girlCardTotal > boyCardTotal) {
        girlCard.classList.add('highlight-card');
    } else if (boyCardTotal > girlCardTotal) {
        boyCard.classList.add('highlight-card');
    }
}

// Запускаем анимацию при загрузке
document.addEventListener('DOMContentLoaded', function() {
    createFloatingElements();
    highlightCardWithHigherTotal();
});