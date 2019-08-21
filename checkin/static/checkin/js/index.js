$(document).ready(function() {
    $('#alertdiv').hide();

    $('#checkinform').on('submit', function(event) {
        event.preventDefault();

        const eventCode = $('#eventcode').val().trim();
        if (eventCode.length != 4) {
            $('#eventcode').addClass('border');
            $('#eventcode').addClass('border-danger');
            return;
        }

        const data = {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'unique_id': eventCode
        }

        $.ajax('/checkin/api/findEvent/', {
            type: 'POST',
            data: data,
            success: (response) => {
                window.location.href = response['url'];
            },
            error: (err) => {
                const responseText = (err.hasOwnProperty('responseText')) ? err.responseText : 'Unknown error: please try again.';
                const alertDiv = $('#alertdiv');
                alertDiv.empty();
                const alert = $('<div class="alert alert-danger" role="alert">' + responseText + '</div>');
                alertDiv.append(alert);
                alertDiv.slideDown(1000).delay(4000).slideUp(1000);
            }
        })
    });

    $('#eventcode').on('change', function() {
        if ($(this).val().length == 4) {
            $(this).addClass('border');
            $(this).addClass('border-success');
            $(this).removeClass('border-danger');
        } else {
            $(this).removeClass('border');
            $(this).removeClass('border-success');
            $(this).removeClass('border-danger');
        }
    });
});