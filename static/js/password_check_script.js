/* 
<----------  Below functions are associated with the register and edit_password page ---------->
*/

let password = document.getElementById('password');
let passwordConfirm = document.getElementById('confirm-password');
let passwordMessage = document.getElementById('password-message');
let button = document.getElementById('submit-button');

// Ensures submit button disabled upon page launch
document.addEventListener("DOMContentLoaded", function () {
    button.disabled = true;
});

/*
Below two functions check the two password fields to see if values match or the opposite 
has an empty value to determine the message displayed and whether button disabled or enabled.
*/
password.addEventListener('keyup', function() {
    if ((password.value != passwordConfirm.value) || (passwordConfirm.value === "")) {
        let html = `<p class="passwordmatch-no">Passwords do not match</p>`;
        passwordMessage.innerHTML = html;
        button.disabled = true;
    } else if (password.value === passwordConfirm.value) {
        let html = `<p class="passwordmatch-yes">Passwords match</p>`;
        passwordMessage.innerHTML = html;
        button.disabled = false;
    }
});

passwordConfirm.addEventListener('keyup', function() {
    if ((password.value != passwordConfirm.value) || (password.value === "")) {
        let html = `<p class="passwordmatch-no">Passwords do not match</p>`;
        passwordMessage.innerHTML =  html;
        button.disabled = true;
    } else if (password.value === passwordConfirm.value) {
        let html = `<p class="passwordmatch-yes">Passwords match </p>`;
        passwordMessage.innerHTML =  html;
        button.disabled = false;
    }
});
