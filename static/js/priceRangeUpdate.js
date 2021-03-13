var slider = document.getElementById("Range");
var output = document.getElementById("PriceRange");
var op = document.getElementById("op");

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  op.innerHTML = this.value;
  output.value = this.value;
}
