document.addEventListener("DOMContentLoaded", function() {
    const categorySelect = document.querySelector("#id_category"); // Подставьте правильный селектор
    const descriptionContainer = document.createElement("div");
    descriptionContainer.id = "category-description-container";
    categorySelect.parentNode.insertBefore(descriptionContainer, categorySelect.nextSibling);

    categorySelect.addEventListener("change", function() {
        const categoryId = this.value;
        fetch(`/events/category-description/${categoryId}/`)
            .then(response => response.json())
            .then(data => {
                descriptionContainer.innerHTML = `<p class="category-description">${data.description}</p>`; // Подставьте правильный ключ для описания
            })
            .catch(error => console.error('Ошибка:', error));
    });
});
