$(document).ready(function () {
    $('#generateForm').on('submit', function (event) {
        event.preventDefault();

        if (confirm('Please confirm that you have deleted all the old statuses before continuing!')) {
            const data = {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'start': $('#start').val(),
                'end': $('#end').val()
            };

            $.ajax('/api/generateIPanelStatus/', {
                type: 'POST',
                data: data,
                success: (response) => {
                    $('#statusModalTitle').html('Success!');
                    const text = (response.failed.length == 0) ? 'Successfully generated all statuses.' : 'The following numbers failed to be generated: ' + response.failed.join(', ');
                    $('#statusModalContent').html(text);
                    $('#statusModal').modal();
                },
                error: (err) => {
                    $('#statusModalTitle').html('Error');
                    $('#statusModalContent').html('Unexpected error generating PNM statuses with text ' + err.responseText + ' Please contact an admin.');
                    $('#statusModal').modal();
                }
            })
        }
    })
})