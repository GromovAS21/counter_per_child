function previewAvatar(input) {
    const preview = document.getElementById('avatar-preview');
    const file = input.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = e => preview.src = e.target.result;
        reader.readAsDataURL(file);
    }
}