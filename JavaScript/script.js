
 

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

var baseURL = getBaseURL('/DBMS'); 

$(function () {
  var header = $.Deferred();
  var footer = $.Deferred();
$('#header').load(baseURL + "/common/header.html"); // load header
$('#footer').load(baseURL + "/common/footer.html"); // load footer
});

function getBaseURL(DBMS) {
  if (window.location.pathname.includes(DBMS)) {
    return window.location.origin + DBMS;
  } else {
    return window.location.origin;
  }
}

$('a[href^="/"], img[src^="/"]').each(function () {
  let filepath = $(this).attr('href');
  let imgpath = $(this).attr('src');
  // Update the href attribute with the relative path
  if (filepath) $(this).attr('href', baseURL + filepath);
  if (imgpath) $(this).attr('src', baseURL + imgpath)
});