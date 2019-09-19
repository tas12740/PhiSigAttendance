const resetForm = function () {
    $('#firstName').val('');
    $('#lastName').val('');
    $('#onyen').val('');
    $('#email').val('');
    $('#pledgeClass').val('');
    $('input[name="preferredContact"]:checked').prop('checked', false);
    $('#phone').val('');
    $('#pronouns').val('');
    $('#house').val('');
    $('#house').selectpicker('refresh');
}

$(document).ready(function () {
    $('#registerForm').on('submit', function (event) {
        event.preventDefault();
        if (confirm('Please confirm that the information you have entered is correct and that you did not put a "s" at the end of your pledge class. This will be the onyen you use to check in for the remainder of your time here. I can change it, but if I have to, I will be cross :).')) {

            const data = {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'first_name': $('#firstName').val(),
                'last_name': $('#lastName').val(),
                'onyen': $('#onyen').val(),
                'email': $('#email').val(),
                'pledge_class': $('#pledgeClass').val(),
                'phone_number': $('#phone').val(),
                'preferred_contact': $('input[name="preferredContact"]:checked').val(),
                'pronouns': $('#pronouns').val(),
                'house': $('#house').val()
            };

            $.ajax('/checkin/register/sibling/', {
                type: 'POST',
                data: data,
                success: () => {
                    $('#registerModalTitle').html('Success!');
                    $('#registerModalContent').html('You have successfully registered.');
                    $('#registerModal').modal();
                    resetForm();
                },
                error: (err) => {
                    const message = (err.hasOwnProperty('responseText')) ? err.responseText : 'Unknown error: please try again later or contact your friendly IT chairs.';
                    $('#registerModalTitle').html('Error');
                    $('#registerModalContent').html(message);
                    $('#registerModal').modal();
                }
            });
        }
    });

});