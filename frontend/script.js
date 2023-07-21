'use strict';


const addEventOnElements = function (elements, eventType, callback) {
  for (let i = 0, len = elements.length; i < len; i++) {
    elements[i].addEventListener(eventType, callback);
  }
}


const preloader = document.querySelector("[data-preloader]");

window.addEventListener("load", function () {
  preloader.classList.add("loaded");
  document.body.classList.add("loaded");
});



const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const overlay = document.querySelector("[data-overlay]");

const toggleNav = function () {
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
  document.body.classList.toggle("nav-active");
}

addEventOnElements(navTogglers, "click", toggleNav);

const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

const activeElementOnScroll = function () {
  if (window.scrollY > 100) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
}

window.addEventListener("scroll", activeElementOnScroll);



const revealElements = document.querySelectorAll("[data-reveal]");

const revealElementOnScroll = function () {
  for (let i = 0, len = revealElements.length; i < len; i++) {
    if (revealElements[i].getBoundingClientRect().top < window.innerHeight / 1.15) {
      revealElements[i].classList.add("revealed");
    } else {
      revealElements[i].classList.remove("revealed");
    }
  }
}

function light_dark_mode() {
  var mode = document.getElementById("mode");
  var btn = document.getElementsByClassName("btn");
  var body = document.body;
  var header = document.getElementsByClassName("header")[0];
  var service = document.getElementsByClassName("service-list")[0];
  var hero = document.getElementsByClassName("hero")[0];
  var about = document.getElementsByClassName("about")[0];
  var footer = document.getElementsByClassName("footer")[0];
  var blog = document.getElementsByClassName("blog-card");
  var logo = document.getElementById("logo-img");



  if (mode.name == "sunny-outline"){
    mode.name = "moon-outline";
  } else{
    mode.name = "sunny-outline";
  }

  if (logo.getAttribute("src") == "./assets/images/fulllogo-darkmode.png"){
    logo.setAttribute("src", "./assets/images/fulllogo-lightmode.png");
  } else{
    logo.setAttribute("src", "./assets/images/fulllogo-darkmode.png");
  }

  body.classList.toggle("light-mode-body");
  header.classList.toggle("light-mode-header");
  hero.classList.toggle("light-mode-hero");
  service.classList.toggle("light-mode-service");
  about.classList.toggle("light-mode-about");
  footer.classList.toggle("light-mode-footer");

  for (var i = 0; i < blog.length; i++) {
    blog[i].classList.toggle("light-mode-blog");
  }
  for (var i = 0; i < btn.length; i++) {
    btn[i].classList.toggle("light-mode-btn");
  }
}

window.addEventListener("scroll", revealElementOnScroll);

window.addEventListener("load", revealElementOnScroll);