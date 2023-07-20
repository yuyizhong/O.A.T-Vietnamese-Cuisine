// Js to display menu details as a modal when required
document.addEventListener('DOMContentLoaded', function() {
    var menuModal = document.getElementById('menuModal');
    var menuModalTitle = document.getElementById('menuModalTitle');
    var menuDescription = document.getElementById('menuDescription');

    menuModal.addEventListener('show.bs.modal', function(event) {
        var button = event.relatedTarget;
        var menuNameValue = button.getAttribute('data-menu-name');
        var menuDescriptionValue = button.getAttribute('data-menu-description');

        menuModalTitle.textContent = menuNameValue;
        menuDescription.textContent = menuDescriptionValue;
    });
});
