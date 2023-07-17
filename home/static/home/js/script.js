document.addEventListener("DOMContentLoaded", function() {
  const containerSections = document.querySelectorAll(".container-section");
  let currentSectionIndex = 0;

  function showNextSection() {
      containerSections[currentSectionIndex].classList.remove("active");
      currentSectionIndex = (currentSectionIndex + 1) % containerSections.length;
      containerSections[currentSectionIndex].classList.add("active");
  }

  // Show the first section initially
  containerSections[currentSectionIndex].classList.add("active");

  // Start the interval to show the next section every 3 seconds
  setInterval(showNextSection, 1500);
});
