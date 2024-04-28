// JavaScript code to filter rooms based on check-in, check-out, and guests
var check_in = '{{ request.args.get("check_in") }}';
var check_out = '{{ request.args.get("check_out") }}';
var guests = '{{ request.args.get("guests") }}';

// Send AJAX request to Flask route with check-in, check-out, and guests data
$.ajax({
    type: 'GET',
    url: '/filter_rooms',
    data: {
        check_in: check_in,
        check_out: check_out,
        guests: guests
    },
    success: function(data) {
        // Populate room cards based on filtered data
        $('#room-cards').html(data);
    }
});


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
  var admin_header = $.Deferred();
$('#header').load(baseURL + "/templates/header.html", function(){ header.resolve() }); // load header
$('#footer').load(baseURL + "/templates/footer.html", function(){ footer.resolve() }); // load footer
$('#admin_header').load(baseURL + "/templates/admin_header.html", function(){ admin_header.resolve() }); // load header

  $.when(header, footer).done(function() {
    $('a[href^="/"], img[src^="/"]').each(function () {
      let filepath = $(this).attr('href');
      let imgpath = $(this).attr('src');
      // Update the href attribute with the relative path
      if (filepath) $(this).attr('href', baseURL + filepath);
      if (imgpath) $(this).attr('src', baseURL + imgpath)
    });
  })
});
function getBaseURL(rootfoldername) {
  if (window.location.pathname.includes(rootfoldername)) {
    return window.location.origin + rootfoldername;
  } else {
    return window.location.origin;
  }
}

function showPassword() {
  var passwordField = document.getElementById("password");
  if (passwordField.type === "password") {
    passwordField.type = "text";
  } else {
    passwordField.type = "password";
 
  }
}