//when scroll up remove class, when scroll down add class
window.addEventListener('scroll', function(){
    let navbar = document.querySelector('.navbar');
    navbar.classList.toggle('scrollHeader', window.scrollY > 0);
  });





$(document).ready(function(){
  $('#link').on("click", function(){
    document.scrollY = 0;
  });
  $(".offcanvas-body ul li h6").on('click', function(){
    $(".offcanvas-body ul li ul").toggleClass("d-block");
  });
})