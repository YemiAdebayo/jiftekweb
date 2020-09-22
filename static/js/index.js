"use strict";

import {
    userInputStripper,
    writeInputErrorMessage,
    removeInputErrorMessage,
    isValidPhoneNumber,
    isValidEmail,
} from "../js/functions.js";


let $html = $("html"),
    $body = $("body");

$(document).ready(function() {

    $('a.home').addClass('active');

    const $slideShow = $("#slideshow");

    const slideMessages = [

        `<div class="slideTextChild">
                    <h1 class=" text-white">
                        <span class="course-intro">WORLD CLASS</span><br>
                        <span id="course-name">CLOUD SOLUTION &amp; SERVICES</span>
                    </h1>
                    <p class="pb-3 pt-1 text-white paragraph" id="course-content">
                        Get the best of cloud computing through Amazon AWS, Microsoft Azure and Google GCP. Let our experts use cloud services to give your business a competitive 
                        advantage by providing the most...
                    </p>
                    <a href="services/cloud-computing" class="blue" id="course-link">
                        MORE DETAILS
                        <span class="pl-2">
                            <i class="fas fa-angle-double-right"></i>
                        </span>
                    </a>
        </div>`,

        `<div class="slideTextChild">
                    <h1 class=" text-white">
                        <span class="course-intro">BESPOKE</span><br>
                        <span id="course-name">WEB &amp; APP DEVELOPMENT</span>
                    </h1>
                    <p class="pb-3 pt-1 text-white paragraph" id="course-content">
                      Step into the world of excellence in designing and developing engaging websites 
                      that tell your brand's unique story. We consult, design & engineer web, 
                      mobile & custom software solutions...
                    </p>
                    <a href="services/web-and-app-design" class="blue" id="course-link">
                        MORE DETAILS
                        <span class="pl-2">
                            <i class="fas fa-angle-double-right"></i>
                        </span>
                    </a>
        </div>`,

        `<div class="slideTextChild">
                    <h1 class=" text-white">
                        <span class="course-intro">SECURITY & COMPLIANCE;</span><br>
                        <span id="course-name">CONSULTING SERVICES</span>
                    </h1>
                    <p class="pb-3 pt-1 text-white paragraph" id="course-content">
                        We identify vulnerabilities in your environment and develop a strategy to remediate & improve
                        your security posture. Our compliance experts can prepare you for industry and regional directives...
                    </p>
                    <a href="services/security-and-compliance" class="blue" id="course-link">
                        MORE DETAILS
                        <span class="pl-2">
                            <i class="fas fa-angle-double-right"></i>
                        </span>
                    </a>
        </div>`,
        `<div class="slideTextChild">
                    <h1 class=" text-white">
                        <span class="course-intro">QUALITY</span><br>
                        <span id="course-name">IT CONSULTING SERVICES</span>
                    </h1>
                    <p class="pb-3 pt-1 text-white paragraph" id="course-content">
                        Developing high impact products that are secure, scalable, meaningful and powerful is what we do.
                        We innovate product development with our expertise across different industries and converging technologies.
                    </p>
                    <a href="services/it-consulting" class="blue" id="course-link">
                        MORE DETAILS
                        <span class="pl-2">
                            <i class="fas fa-angle-double-right"></i>
                        </span>
                    </a>
        </div>`,
    ];

    $slideShow.vegas({
        delay: 8000,
        preload: true,
        timer: false,
        shuffle: false,
        cover: true,
        firstTransition: "fade",
        firstTransitionDuration: 20,
        transition: "fade",
        transitionDuration: 4000,
        slides: [{
                src: "/static/img/best-cloud-solution-and-consultancy-service-in-lagos.webp"
            },
            {
                src: "/static/img/cloud-and-IT-services.webp"
            },
            {
                src: "/static/img/excellent-IT-security-and-consultancy-services.webp"
            },
            // {
            //     src: "/static/img/web-development-and-enterprise-solutions.webp"
            // },
            {
                src: "/static/img/information-technology-consulting-services.webp"
            },
        ],
        overlay: "/static/img/01.png",

        walk: function(index) {

            // $('#slideText').fadeOut(1500, function () {
            //     $('.slideTextChild').replaceWith(
            //         slideMessages[index]
            //     )
            // }).fadeIn(1500);

            $('.slideTextChild').replaceWith(
                slideMessages[index]
            );
        },
    });

    $('input, textarea').each(function() {
        $(this).focus(function() {
            $(this).prev().addClass("in-focus");
        });
    });

    $(".error-handler").each(function() {
        $(this).blur(function() {
            var $this = $(this);
            writeInputErrorMessage($this);
        })
        $(this).focus(function() {
            var $this = $(this);
            removeInputErrorMessage($this);
        })
    })

    let $submitBtn = $(".submit-button");
    $submitBtn.click(function(e) {
        e.preventDefault();

        var $full_name = $('.full-name'),
            $email = $(".email"),
            $phoneNum = $(".phone-number"),
            $message = $(".message");

        var clean_Fullname = userInputStripper($('.full-name').val()),
            clean_message = userInputStripper($('.message').val());
        $full_name.val(clean_Fullname);
        $message.val(clean_message);

        $(".error-handler").each(function() {
            var $this = $(this);
            writeInputErrorMessage($this);
        })

        var $allWarning = $(".inquiry-form").find(".warning");

        if (parseInt($allWarning.length) > 0) {
            $($html, $body).animate({
                scrollTop: $("fieldset:nth-of-type(1)").offset().top
            }, 1200, false);
        } else if (!isValidPhoneNumber($phoneNum.val())) {
            $phoneNum.after($("<span class='warning paragraph'>This contact number is invalid!</span> ").css("display", "inline-block"));
        } else if (!isValidEmail($email.val())) {
            $email.after($("<span class='warning paragraph'>This email is invalid!</span> ").css("display", "inline-block"));
        } else {
            $('.inquiry-form').unbind('submit').submit();
        }
    });
})