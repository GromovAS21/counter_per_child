// Создаем плавающие элементы с улучшенной анимацией
function createFloatingElements() {
    const colors = [
        'rgba(255, 105, 180, 0.7)', 'rgba(255, 182, 193, 0.7)',
        'rgba(219, 112, 147, 0.7)', 'rgba(255, 192, 203, 0.7)',
        'rgba(100, 181, 246, 0.7)', 'rgba(66, 165, 245, 0.7)',
        'rgba(30, 136, 229, 0.7)', 'rgba(144, 202, 249, 0.7)'
    ];

    const container = document.getElementById('floating-elements');
    const elements = ['🧸', '🍼', '👚', '👕', '?', '？'];

    // Очищаем старые элементы перед созданием новых
    container.innerHTML = '';

    // Увеличиваем количество элементов для более частого падения
    for (let i = 0; i < 50; i++) {
        const element = document.createElement('div');
        element.className = 'floating-element';

        // Размер и позиция
        const size = Math.random() * 30 + 20;
        const startX = Math.random() * 100;
        const startY = -size;

        // Параметры анимации
        const duration = Math.random() * 15 + 10;
        const delay = Math.random() * 5;
        const rotation = Math.random() * 360;
        const color = colors[Math.floor(Math.random() * colors.length)];

        // Настройка элемента
        element.style.width = `${size}px`;
        element.style.height = `${size}px`;
        element.style.left = `${startX}vw`;
        element.style.top = `${startY}px`;
        element.style.animation = `fall-animation ${duration}s linear ${delay}s infinite`;
        element.style.setProperty('--start-x', `${startX}vw`);
        element.style.setProperty('--end-x', `${getEndX(startX)}vw`);
        element.style.setProperty('--rotation', `${rotation}deg`);
        element.style.transform = `rotate(${rotation}deg)`;
        element.style.willChange = 'transform, opacity';

        // Выбираем тип элемента
        const elementType = Math.random();
        if (elementType < 0.6) {
            // Эмодзи
            const emoji = elements[Math.floor(Math.random() * 4)];
            element.textContent = emoji;
            element.style.fontSize = `${size * 0.8}px`;
            element.style.color = color;
        } else if (elementType < 0.9) {
            // Вопросительные знаки
            const questionMark = elements[4 + Math.floor(Math.random() * 2)];
            element.textContent = questionMark;
            element.style.fontSize = `${size}px`;
            element.style.color = color;
            element.style.fontFamily = 'Arial, sans-serif';
            element.style.fontWeight = 'bold';
            element.style.textShadow = '0 2px 4px rgba(0,0,0,0.2)';
        } else {
            // Только круг из геометрических фигур
            element.style.backgroundColor = color;
            element.style.borderRadius = '50%';
        }

        container.appendChild(element);
    }
}

// Функция для определения конечной позиции по X
function getEndX(startX) {
    const movementType = Math.floor(Math.random() * 6);
    switch (movementType) {
        case 0: return startX + Math.random() * 20;
        case 1: return startX - Math.random() * 20;
        case 2: return startX + (Math.random() * 40 - 20);
        case 3: return startX + Math.sin(startX / 10) * 30;
        case 4: return startX + (Math.random() > 0.5 ? 1 : -1) * 25;
        default: return startX;
    }
}

// Добавляем CSS анимацию
const style = document.createElement('style');
style.innerHTML = `
    @keyframes fall-animation {
        0% {
            transform: translate(var(--start-x), -50px) rotate(0deg);
            opacity: 0;
        }
        10% {
            opacity: 0.8;
        }
        90% {
            opacity: 0.8;
        }
        100% {
            transform: translate(var(--end-x), calc(100vh + 50px)) rotate(var(--rotation));
            opacity: 0;
        }
    }
    
    .floating-element {
        position: fixed;
        z-index: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        pointer-events: none;
        animation-timing-function: linear;
    }
`;
document.head.appendChild(style);

// Функция для анимации изменения числа с цветом
function animateNumberChange(elementId, newValue, isIncrease) {
    const element = document.getElementById(elementId);
    const startValue = parseInt(element.textContent) || 0;
    const duration = 500;
    const startTime = performance.now();

    // Устанавливаем начальный цвет
    element.style.color = isIncrease ? '#4CAF50' : '#F44336';

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const currentValue = Math.floor(startValue + (newValue - startValue) * progress);

        element.textContent = currentValue;

        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            // Возвращаем обычный цвет через небольшой промежуток времени
            setTimeout(() => {
                element.style.color = '';
            }, 300);
        }
    }

    requestAnimationFrame(update);
}

document.addEventListener('DOMContentLoaded', function () {
    createFloatingElements();
    updateLeadingCard();
});