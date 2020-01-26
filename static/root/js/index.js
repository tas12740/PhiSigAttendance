$(document).ready(function () {
    $('.carousel').carousel({
        ride: true,
        pause: false
    });

    const width = $('.carousel-img').width();
    // 13/5 = curr_width/curr_height => curr_height = curr_width*5/13
    const new_height = width * 5 / 13;
    $('.carousel-img').height(new_height);
    $('.carousel-img').css('min-height', new_height);
    $('.carousel-img').css('max-height', new_height);

    $(window).resize(function () {
        const width = $('.carousel-img').width();
        const new_height = width * 5 / 13;
        $('.carousel-img').height(new_height);
        $('.carousel-img').css('min-height', new_height);
        $('.carousel-img').css('max-height', new_height);
    });
})