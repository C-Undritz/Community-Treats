let oneStars = document.getElementById('star1');
let twoStars = document.getElementById('star2');
let threeStars = document.getElementById('star3');
let fourStars = document.getElementById('star4');
let fiveStars = document.getElementById('star5');
let starPanel = document.getElementById('star-panel');
let ratingSelected = false;
let rate = document.getElementById('rating-text');
let ratingArea = document.getElementById('rating-area');

document.addEventListener("DOMContentLoaded", function () {
    ratingArea.style.display = "none";
    oneStars.setAttribute('class', 'fas fa-star fa-2x');
    twoStars.setAttribute('class', 'fas fa-star fa-2x');
    threeStars.setAttribute('class', 'fas fa-star fa-2x');
    fourStars.setAttribute('class', 'fas fa-star fa-2x');
    fiveStars.setAttribute('class', 'fas fa-star fa-2x');
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
});

rate.addEventListener('click', function () {
    if (ratingArea.style.display === "none") {
        ratingArea.style.display = "block";
    } else {
        ratingArea.style.display = "none";
    }
});

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

let resetRating = function () {
    ratingSelected = false;
    console.log(ratingSelected);
}

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

starPanel.onmouseenter = resetRating;

oneStars.addEventListener('click', function () {
    oneStars.style.color = 'orange';
    twoStars.style.color = '#FCF3E9';
    threeStars.style.color = '#FCF3E9';
    fourStars.style.color = '#FCF3E9';
    fiveStars.style.color = '#FCF3E9';
    ratingSelected = true;
    console.log(ratingSelected);
});

twoStars.addEventListener('click', function () {
    oneStars.style.color = 'orange';
    twoStars.style.color = 'orange';
    threeStars.style.color = '#FCF3E9';
    fourStars.style.color = '#FCF3E9';
    fiveStars.style.color = '#FCF3E9';
    ratingSelected = true;
    console.log(ratingSelected);
});

threeStars.addEventListener('click', function () {
    oneStars.style.color = 'orange';
    twoStars.style.color = 'orange';
    threeStars.style.color = 'orange';
    fourStars.style.color = '#FCF3E9';
    fiveStars.style.color = '#FCF3E9';
    ratingSelected = true;
    console.log(ratingSelected);
});

fourStars.addEventListener('click', function () {
    oneStars.style.color = 'orange';
    twoStars.style.color = 'orange';
    threeStars.style.color = 'orange';
    fourStars.style.color = 'orange';
    fiveStars.style.color = '#FCF3E9';
    ratingSelected = true;
    console.log(ratingSelected);
});

fiveStars.addEventListener('click', function () {
    oneStars.style.color = 'orange';
    twoStars.style.color = 'orange';
    threeStars.style.color = 'orange';
    fourStars.style.color = 'orange';
    fiveStars.style.color = 'orange';
    ratingSelected = true;
    console.log(ratingSelected);
});
