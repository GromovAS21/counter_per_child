// Управление меню
const menuBtn = document.getElementById('menuBtn');
const menuDropdown = document.getElementById('menuDropdown');

menuBtn.addEventListener('click', function (e) {
    e.stopPropagation();
    menuDropdown.classList.toggle('active');
});

// Закрытие меню при клике вне его
document.addEventListener('click', function () {
    menuDropdown.classList.remove('active');
});

// Предотвращаем закрытие меню при клике на него
menuDropdown.addEventListener('click', function (e) {
    e.stopPropagation();
});

document.addEventListener('DOMContentLoaded', function () {
    const userNameContainers = document.querySelectorAll('.user-name-container');

    userNameContainers.forEach(container => {
        const userName = container.querySelector('.user-name');
        if (userName.scrollWidth > container.offsetWidth) {
            container.classList.add('long-text');
        }
    });
});