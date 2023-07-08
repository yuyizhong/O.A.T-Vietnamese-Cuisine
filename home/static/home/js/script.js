document.addEventListener("DOMContentLoaded", function() {
  var containerSections = document.querySelectorAll(".container-section");
  var delay = 0;

  containerSections.forEach(function(section) {
    setTimeout(function() {
      section.style.opacity = "1";
      section.style.transform = "translateY(0)";
    }, delay);

    delay += 200;
  });
});