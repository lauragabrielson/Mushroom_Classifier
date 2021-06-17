// found this code one w3 schools. Works great.

var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
  // This function will display the specified tab of the form ...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  // ... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  // ... and run a function that displays the correct step indicator:
  fixStepIndicator(n)
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form... :
  if (currentTab >= x.length) {
    //...the form gets submitted:

    var form = document.querySelector('#predictForm');
    var data = new FormData(form);
    var req = new XMLHttpRequest();
    req.onload = function(e){

      function convertResult(result) {

        var answer = result;

        var resultArray = []
  
        if (answer == "EE") {
          resultArray = ["Europe" , "Edible"];
        }
        if (answer == "EP") {
          resultArray = ["Europe" , "Poisonous"];
        }
        if (answer == "NE") {
          resultArray = ["North America" , "Edible"];
        }
        if (answer == "NP") {
          resultArray = ["North America" , "Poisonous"];
        }

        return resultArray
      }

      function showResult(result) {
        var window = document.getElementById("result-window");
        var image = document.getElementById("result-image");

        var answer = result;

        if (window.style.display === "none") {
          window.style.display = "block";
        } else {
          window.style.display = "none";
        }

        if (answer == "Edible") {
          window.classList.add("edible");
          image.src = "https://media1.tenor.com/images/65cf2fae3c9167c43e08c93c581b631d/tenor.gif?itemid=11918844";
        } else {
          window.classList.add("poisonous");
          image.src = "../static/images/skull.gif";
        }
      }

      function hideButtons() {
        var nextBtn = document.getElementById("nextBtn");
        nextBtn.style.display = "none";

        var prevBtn = document.getElementById("prevBtn");
        prevBtn.style.display = "none";

        var formIntro = document.getElementById("form-intro");
        formIntro.style.display = "none";
      }

      result = e.currentTarget.response

      resultContinent = convertResult(result)[0];
      resultClass = convertResult(result)[1];

      // // document.getElementById("result_window")
      document.getElementById("mushroom-class").innerText = resultClass;
      document.getElementById("mushroom-continent").innerText = resultContinent;

      convertResult(result);
      hideButtons(result);
      showResult(result);

    };
    req.open("POST", "/predict");
    req.send(data);
  
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false:
      valid = false;
    }
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }

  return valid; // return the valid status
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class to the current step:
  x[n].className += " active";
}