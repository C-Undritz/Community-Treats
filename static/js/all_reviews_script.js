let latestReviewsTitle = document.getElementById('latest-reviews-title');
let allReviewsTitle = document.getElementById('all-reviews-title');
let revealReviews = document.getElementById('reveal-all-reviews');
let hideReviews = document.getElementById('hide-all-reviews');
let allReviewsText  = document.getElementById('all-reviews');

document.addEventListener("DOMContentLoaded", function () {
    allReviewsTitle.style.display = "none";
    hideReviews.style.display = "none";
    allReviewsText.style.display = "none";
});

revealReviews.addEventListener('click', function () {
    latestReviewsTitle.style.display = "none";
    allReviewsTitle.style.display = "block";
    revealReviews.style.display = "none";
    hideReviews.style.display = "block";
    allReviewsText.style.display = "block";
});

hideReviews.addEventListener('click', function() {
    latestReviewsTitle.style.display = "block";
    allReviewsTitle.style.display = "none";
    revealReviews.style.display = "block";
    hideReviews.style.display = "none";
    allReviewsText.style.display = "none";
});