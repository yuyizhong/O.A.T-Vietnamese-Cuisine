document.addEventListener("DOMContentLoaded", function() {
    var containerSections = document.querySelectorAll(".container-section");
    var currentIndex = 0;

    // Show the first container-section initially
    containerSections[currentIndex].style.display = "flex";

    setInterval(function() {
        // Hide the current container-section
        containerSections[currentIndex].style.display = "none";

        // Increment the currentIndex
        currentIndex++;

        // Reset the index to 0 if it exceeds the number of container-sections
        if (currentIndex >= containerSections.length) {
            currentIndex = 0;
        }

        // Show the next container-section
        containerSections[currentIndex].style.display = "flex";
    }, 5000);
});