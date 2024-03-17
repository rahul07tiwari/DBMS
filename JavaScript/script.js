  // crousel........swiper
  var swiper = new Swiper(".swiper-container", {
    spaceBetween: 30,
    effect: "fade",
    loop:true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },
  });
//testimonials......... swiper
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

  //-------------------------------load header and footer in main html page-------------------------------------------------------//
  $(function () {
    var header = $.Deferred();
    var footer = $.Deferred();
    $('#header').load(baseURL + "/HTML/header.html", function () { header.resolve(); }); // load header
    $('#footer').load(baseURL + "/HTML/footer.html", function () { footer.resolve(); }); // load footer
  });
  
