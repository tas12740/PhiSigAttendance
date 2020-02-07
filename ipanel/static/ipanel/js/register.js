$(document).ready(function () {
    $('#registerForm').on('submit', function (event) {
        event.preventDefault();

        const checked = $('#check').prop('checked');

        if (!checked) {
            alert('You must acknowledge that you have submitted and understand the Subrosa form!');
            return;
        }

        const data = {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'onyen': $('#onyen').val()
        }

        $.ajax('/api/ipanelRegister/', {
            type: 'POST',
            data: data,
            success: (response) => {
                $('#registerModalTitle').html('Success!');
                $('#registerModalContent').html('Your passcode is ' + response.code + '. Please copy this code somewhere secret and hold onto it, as it will remain your passcode for the remainder of this IPanel.');
                $('#registerModal').modal();
                $('#onyen').val('');
                $('#check').prop('checked', false);
            },
            error: (err) => {
                $('#registerModalTitle').html('Error!');
                if (err.status == 500) {
                    $('#registerModalContent').html('Apparently there is a server error going on currently ... stick with us in these trying times')
                } else if (err.responseJSON.hasOwnProperty('code')) {
                    $('#registerModalContent').html('Your passcode is ' + err.responseJSON['code'] + '. Please copy this code somewhere secret and hold onto it, as it will remain your passcode for the remainder of this IPanel.');
                    $('#onyen').val('');
                    $('#check').prop('checked', false);
                } else {
                    $('#registerModalContent').html(err.responseText);
                }
                $('#registerModal').modal();
            }
        })
    });
})