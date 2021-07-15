/* 
<----------  Below functions are associated with the view_recipe.html page ---------->
These functions allow the user to rate the viewed recipe out of five using an interactive display of an array of
five stars.  The stars go from displaying as clear to the colour orange as the user mouses over them.  Once the 
user clicks on a star to indicate their chosen score, the star clicked and those before it will remain orange. 
The user can then click on the submit button to have the database record their rating.  The stars can be reset by 
moving the mouse cursor over the stars array and then moving the cursor away. Governing this is a variable 
'ratingSelected' that changes the behaviour whether it is 'true' or 'false'.
*/

let oneStars = document.getElementById('star1');
let twoStars = document.getElementById('star2');
let threeStars = document.getElementById('star3');
let fourStars = document.getElementById('star4');
let fiveStars = document.getElementById('star5');
let starPanel = document.getElementById('star-panel');
let ratingSelected = false;
let rate = document.getElementById('rating-text');
let ratingArea = document.getElementById('rating-area');
let ratingSubmit = document.getElementById('rating-submit-btn');

document.addEventListener("DOMContentLoaded", function () {
    ratingArea.style.display = "none";
    oneStars.setAttribute('class', 'fas fa-star rating-star');
    twoStars.setAttribute('class', 'fas fa-star rating-star');
    threeStars.setAttribute('class', 'fas fa-star rating-star');
    fourStars.setAttribute('class', 'fas fa-star rating-star');
    fiveStars.setAttribute('class', 'fas fa-star rating-star');
    oneStars.style.textShadow = '-1px 1px 2px #ee6e73, 1px 1px 2px #ee6e73, 1px -1px 0 #ee6e73, -1px -1px 0 #ee6e73';
    oneStars.style.color = '#FCF3E9';
    twoStars.style.textShadow = '-1px 1px 2px #ee6e73, 1px 1px 2px #ee6e73, 1px -1px 0 #ee6e73, -1px -1px 0 #ee6e73';
    twoStars.style.color = '#FCF3E9';
    threeStars.style.textShadow = '-1px 1px 2px #ee6e73, 1px 1px 2px #ee6e73, 1px -1px 0 #ee6e73, -1px -1px 0 #ee6e73';
    threeStars.style.color = '#FCF3E9';
    fourStars.style.textShadow = '-1px 1px 2px #ee6e73, 1px 1px 2px #ee6e73, 1px -1px 0 #ee6e73, -1px -1px 0 #ee6e73';
    fourStars.style.color = '#FCF3E9';
    fiveStars.style.textShadow = '-1px 1px 2px #ee6e73, 1px 1px 2px #ee6e73, 1px -1px 0 #ee6e73, -1px -1px 0 #ee6e73';
    fiveStars.style.color = '#FCF3E9';
    ratingSubmit.disabled = true;
});

// Shows the rating stars array and submit button upon the user clicking on the text 'leave rating'.
rate.addEventListener('click', function () {
    if (ratingArea.style.display === "none") {
        ratingArea.style.display = "block";
    } else {
        ratingArea.style.display = "none";
    }
});

// The following functions temporarily change the current star to orange along with any preceeding stars when called.
let mouseOverFunctionOne = function () {
    this.style.color = 'orange';
};

let mouseOutFunctionOne = function () {
    if (ratingSelected == false) {
        this.style.color = '#FCF3E9';
    }
};

let mouseOverFunctionTwo = function () {
    this.style.color = 'orange';
    oneStars.style.color = 'orange';
};

let mouseOutFunctionTwo = function () {
    if (ratingSelected == false) {
        this.style.color = '#FCF3E9';
        oneStars.style.color = '#FCF3E9';
    }
};

let mouseOverFunctionThree = function () {
    this.style.color = 'orange';
    oneStars.style.color = 'orange';
    twoStars.style.color = 'orange';
};

let mouseOutFunctionThree = function () {
    if (ratingSelected == false) {
        this.style.color = '#FCF3E9';
        oneStars.style.color = '#FCF3E9';
        twoStars.style.color = '#FCF3E9';
    }
};

let mouseOverFunctionFour = function () {
    this.style.color = 'orange';
    oneStars.style.color = 'orange';
    twoStars.style.color = 'orange';
    threeStars.style.color = 'orange';
};

let mouseOutFunctionFour = function () {
    if (ratingSelected == false) {
        this.style.color = '#FCF3E9';
        oneStars.style.color = '#FCF3E9';
        twoStars.style.color = '#FCF3E9';
        threeStars.style.color = '#FCF3E9';
    }
};

let mouseOverFunctionFive = function () {
    this.style.color = 'orange';
    oneStars.style.color = 'orange';
    twoStars.style.color = 'orange';
    threeStars.style.color = 'orange';
    fourStars.style.color = 'orange';
};

let mouseOutFunctionFive = function () {
    if (ratingSelected == false) {
        this.style.color = '#FCF3E9';
        oneStars.style.color = '#FCF3E9';
        twoStars.style.color = '#FCF3E9';
        threeStars.style.color = '#FCF3E9';
        fourStars.style.color = '#FCF3E9';
    }
};

// Reset the star rating to false and therefore the stars colours to clear. Rating button also disabled.
let resetRating = function () {
    ratingSelected = false;
    ratingSubmit.disabled = true;
};

// Calls the functions to change the stars colours when moused over.
oneStars.onmouseover = mouseOverFunctionOne;
oneStars.onmouseout = mouseOutFunctionOne;

twoStars.onmouseover = mouseOverFunctionTwo;
twoStars.onmouseout = mouseOutFunctionTwo;

threeStars.onmouseover = mouseOverFunctionThree;
threeStars.onmouseout = mouseOutFunctionThree;

fourStars.onmouseover = mouseOverFunctionFour;
fourStars.onmouseout = mouseOutFunctionFour;

fiveStars.onmouseover = mouseOverFunctionFive;
fiveStars.onmouseout = mouseOutFunctionFive;

// Calls the function to reset rating prior to submission on mouse enter
starPanel.onmouseenter = resetRating;

/* The following functions change the current star to orange along with any preceeding stars when they are clicked 
and the submit button is also enabled.  This is when a rating value has been selected in the HTML. ratingSelected is 
then true and the resetRating() function is then required to reset the stars. The rating value is kepted, however the 
button is disabled until the user selects a new rating so as to prevent the previous rating value from being recorded. */
oneStars.addEventListener('click', function () {
    oneStars.style.color = 'orange';
    twoStars.style.color = '#FCF3E9';
    threeStars.style.color = '#FCF3E9';
    fourStars.style.color = '#FCF3E9';
    fiveStars.style.color = '#FCF3E9';
    ratingSelected = true;
    ratingSubmit.disabled = false;
});

twoStars.addEventListener('click', function () {
    oneStars.style.color = 'orange';
    twoStars.style.color = 'orange';
    threeStars.style.color = '#FCF3E9';
    fourStars.style.color = '#FCF3E9';
    fiveStars.style.color = '#FCF3E9';
    ratingSelected = true;
    ratingSubmit.disabled = false;
});

threeStars.addEventListener('click', function () {
    oneStars.style.color = 'orange';
    twoStars.style.color = 'orange';
    threeStars.style.color = 'orange';
    fourStars.style.color = '#FCF3E9';
    fiveStars.style.color = '#FCF3E9';
    ratingSelected = true;
    ratingSubmit.disabled = false;
});

fourStars.addEventListener('click', function () {
    oneStars.style.color = 'orange';
    twoStars.style.color = 'orange';
    threeStars.style.color = 'orange';
    fourStars.style.color = 'orange';
    fiveStars.style.color = '#FCF3E9';
    ratingSelected = true;
    ratingSubmit.disabled = false;
});

fiveStars.addEventListener('click', function () {
    oneStars.style.color = 'orange';
    twoStars.style.color = 'orange';
    threeStars.style.color = 'orange';
    fourStars.style.color = 'orange';
    fiveStars.style.color = 'orange';
    ratingSelected = true;
    ratingSubmit.disabled = false;
});