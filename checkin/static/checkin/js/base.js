$(document).ready(function() {
    $(document).ajaxStart(function() {
        $('#loader').show();
        $('body').css('opacity', 0.5);
        $(':input').prop('disabled', true);
        $('a').on('click', function(e) {
            e.preventDefault();
        })
    });
    $(document).ajaxComplete(function() {
        $('#loader').hide();
        $('body').css('opacity', 1.0);
        $(':input').prop('disabled', false);
        $('a').unbind();
    })
});