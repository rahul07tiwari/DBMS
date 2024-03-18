
 

//----------------------------------------crousel........swiper-------------------------------------------------//
  var swiper = new Swiper(".swiper-container", {
    spaceBetween: 30,
    effect: "fade",
    loop:true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },
  });
//-----------------------------------------testimonials......... swiper-----------------------------------------//
  var swiper = new Swiper(".swiper-testimonials", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    slidesperview: "3",
    loop: true,
    coverflowEffect: {
      rotate: 50,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows: false,
    },
    pagination: {
      el: ".swiper-pagination",
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
      },
      640: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    }
  });
//-------------------------------------------facilities......... swiper-------------------------------------//
  var swiper = new Swiper(".mySwiper", {
    spaceBetween: 40,
    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
      },
      640: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    }
  });
//----------------------------------------header and footer loading---------------------------------------------//

document.addEventListener("DOMContentLoaded", function() {
  
  //--------------------------------------Load header.html------------------------------------------------------//
  fetch("./HTML/header.html")
      .then(response => response.text())
      .then(data => {
          document.getElementById("header").innerHTML = data;
      });

  //-------------------------------------Load footer.html-------------------------------------------------------//
  fetch("./HTML/footer.html")
      .then(response => response.text())
      .then(data => {
          document.getElementById("footer").innerHTML = data;
      });
});

 
  
