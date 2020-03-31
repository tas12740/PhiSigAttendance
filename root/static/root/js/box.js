const resetForm = () => {
    $('#submission').val('');
}

$(document).ready(function () {
    $('#box-form').on('submit', function (e) {
        e.preventDefault();

        const submission = $('#submission').val();

        const data = {
            'submission': submission,
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
        }

        $.ajax('/api/box/', {
            type: 'POST',
            data: data,
            success: () => {
                $('#modalTitle').html('Success!');
                $('#modalContent').html('Your submission was successful.');
                $('#modal').modal();
                resetForm();
            },
            error: (err) => {
                const message = (err.hasOwnProperty('responseText')) ? err.responseText : 'Unknown error: please try again later or contact your friendly IT chairs.';
                $('#modalTitle').html('Error');
                $('#modalContent').html(message);
                $('#modal').modal();
            }
        });
    })
})