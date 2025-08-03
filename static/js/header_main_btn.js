 // Управление меню
    const menuBtn = document.getElementById('menuBtn');
    const menuDropdown = document.getElementById('menuDropdown');

    menuBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        menuDropdown.classList.toggle('active');
    });

    // Закрытие меню при клике вне его
    document.addEventListener('click', function() {
        menuDropdown.classList.remove('active');
    });

    // Предотвращаем закрытие меню при клике на него
    menuDropdown.addEventListener('click', function(e) {
        e.stopPropagation();
    });