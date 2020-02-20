$(document).ready(function () {
    $(document).ajaxStart(function () {
        $('#loader').show();
        $('body').css('opacity', 0.5);
        $(':input').prop('disabled', true);
    });
    $(document).ajaxComplete(function () {
        $('#loader').hide();
        $('body').css('opacity', 1.0);
        $(':input').prop('disabled', false);
    })
});