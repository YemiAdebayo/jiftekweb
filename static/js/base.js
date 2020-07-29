"use strict";

$(document).ready(function () {
    let $mainNav = $("#mainNav"),
        $navTriggerBtn = $("#navTriggerBtn"),
        $mainNavWrapper = $(".mainNav-wrapper");

    $navTriggerBtn.click(function () {
        $mainNav.toggleClass("active");
        $mainNavWrapper.toggleClass("active");
    });

    let fadeOut = document.querySelectorAll('.animate-into-view');
    let intersectionObserver = new IntersectionObserver(entries => {
        // If intersectionRatio is 0, the sentinel is out of view
        // and we do not need to do anything.

        entries.forEach(entry => {
            if (entry.intersectionRatio > 0) {
                entry.target.classList.add('fadeIn');
                intersectionObserver.unobserve(entry.target);
            };
        });
    });

    if (fadeOut) {
        fadeOut.forEach(element => {
            intersectionObserver.observe(element);
        });
    };

})