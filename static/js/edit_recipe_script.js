/* 
<----------  Below functions are associated with the edit_recipe.html page ---------->
*/

// Deletes the existing(populated) ingredient and instruction elements when user clicks on 
// the 'bin' icons (during an edit)
// The below was learnt from flaviocopes.com article: "How to add an event listener to multiple 
// elements in JavaScript" (https://flaviocopes.com/how-to-add-event-listener-multiple-elements-javascript/)
document.querySelectorAll('.delete-existing').forEach(item => {
    item.addEventListener('click', event => {
        let existingParent = item.parentElement.parentElement.parentElement;
        existingParent.remove();
        console.log(item)
    });
});

// Deletes the added ingredient and instruction elements when user clicks on the 'bin' icons
function deleteAddedElement() {
    let parent = this.parentElement.parentElement;
    parent.remove();
}

// Event listeners for the 'add ingredient' and 'add instruction' buttons
let addIngredient = document.querySelector('#add-ingredient');
let addInstruction = document.querySelector('#add-instruction');

// Creates the form input element for an additional ingredient when button clicked
addIngredient.addEventListener('click', function () {
    let parent = document.querySelector('#additional-ingredients-here');
    let html = `<div class="row">
                    <div class="col s12">
                        <div class="input-field col s11">
                            <i class="fas fa-hand-point-right prefix icon-style"></i>
                            <input id="ingredient" name="ingredient" type="text" class="validate" required>
                            <label for="ingredient">Additional ingredient</label>
                        </div>
                        <div class="col s1">
                            <button type="button" class="icon-style delete-added"><i class="fas fa-trash-alt"></i></button>
                        </div>
                    </div>
                </div>`
    let template = document.createElement('div');
    template.innerHTML = html;
    let finalHTML = template.firstChild;
    finalHTML.querySelector('.delete-added').addEventListener('click', deleteAddedElement);
    parent.appendChild(finalHTML);
});

// Creates the form input element for an additional instruction when button clicked
addInstruction.addEventListener('click', function () {
    let parent = document.querySelector('#additional-instructions-here');
    let html = `<div class="row">
                    <div class="col s12">
                        <div class="input-field col s11">
                            <i class="fas fa-thumbs-up prefix icon-style"></i>
                            <input id="instruction" name="instruction" type="text" class="validate" required>
                            <label for="instruction">Additional step</label>
                        </div>
                        <div class="col s1">
                            <button type="button" class="icon-style delete-added"><i class="fas fa-trash-alt"></i></button>
                        </div>
                    </div>
                </div>`
    let template = document.createElement('div');
    template.innerHTML = html;
    let finalHTML = template.firstChild;
    finalHTML.querySelector('.delete-added').addEventListener('click', deleteAddedElement);
    parent.appendChild(finalHTML);
});