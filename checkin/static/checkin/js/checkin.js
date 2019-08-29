const resetForm = function() {
    $('#onyen').val('');
}

$(document).ready(function() {
    $('#checkinForm').on('submit', function(event) {
        event.preventDefault();

        const data = {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'event_code': $('#eventCode').val(),
            'onyen': $('#onyen').val()
        }

        $.ajax('/api/checkin/', {
            type: 'POST',
            data: data,
            success: () => {
                $('#checkinModalTitle').html('Success!');
                $('#checkinModalContent').html('Your checkin was successful.');
                $('#checkinModal').modal();
                resetForm();
            },
            error: (err) => {
                const message = (err.hasOwnProperty('responseText')) ? err.responseText : 'Unknown error: please try again later or contact your friendly IT chairs.';
                $('#checkinModalTitle').html('Error');
                $('#checkinModalContent').html(message);
                $('#checkinModal').modal();
            }
        })
    })
});