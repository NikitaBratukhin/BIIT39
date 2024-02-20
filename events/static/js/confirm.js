document.addEventListener("DOMContentLoaded", function() {
  const form = document.querySelector("form");
  form.onsubmit = function(event) {
    event.preventDefault();
    const isConfirmed = confirm("Вы уверены, что хотите создать эту категорию?");
    if (isConfirmed) {
      form.submit();
    }
  };
});
