document.addEventListener('DOMContentLoaded', function () {
  // Materialize required JS for the mobile sidenav
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems, {
    edge: "right"
  });

  // Materialize required JS for the Forms 'select' function
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems, {});
});

/* 
<----------  Below functions are associated with the add_recipe.html page ---------->
*/
// Deletes the added ingredient and instruction elements when user clicks on the 'bin' icon
function deleteElement() {
  let parent = this.parentElement.parentElement;
  parent.remove();
}

// Event listeners for the 'add ingredient' and 'add instruction' buttons
let addIngredient = document.querySelector('#add-ingredient');
let addInstruction = document.querySelector('#add-instruction');

// Creates the form input element for an additional ingredient when button clicked
addIngredient.addEventListener('click', function() {
  let parent = document.querySelector('#additional-ingredients-here');
  let html = `<div class="row">
                <div class="col s12">
                  <div class="input-field col s11">
                    <i class="fas fa-hand-point-right prefix icon-style"></i>
                    <input id="ingredient" name="ingredient" type="text" class="validate" required>
                    <label for="ingredient">Additional ingredient</label>
                  </div>
                  <div class="col s1">
                    <button type="button" class="icon-style delete"><i class="fas fa-trash-alt"></i></button>
                  </div>
                </div>
              </div>`
  let template = document.createElement('div');
  template.innerHTML = html;
  let finalHTML = template.firstChild;
  finalHTML.querySelector('.delete').addEventListener('click', deleteElement);
  parent.appendChild(finalHTML);
});

// Creates the form input element for an additional instruction when button clicked
addInstruction.addEventListener('click', function() {
  let parent = document.querySelector('#additional-instructions-here');
  let html = `<div class="row">
                <div class="col s12">
                  <div class="input-field col s11">
                    <i class="fas fa-thumbs-up prefix icon-style"></i>
                    <input id="instruction" name="instruction" type="text" class="validate" required>
                    <label for="instruction">Additional step</label>
                  </div>
                  <div class="col s1">
                    <button type="button" class="icon-style delete"><i class="fas fa-trash-alt"></i></button>
                  </div>
                </div>
              </div>`
  let template = document.createElement('div');
  template.innerHTML = html;
  let finalHTML = template.firstChild;
  finalHTML.querySelector('.delete').addEventListener('click', deleteElement);
  parent.appendChild(finalHTML);
});

