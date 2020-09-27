$(document).ready(function () {
    $('#delete-old').on('click', function (event) {
        event.preventDefault();

        if (confirm('WARNING! THIS WILL DELETE VOTES AND CANNOT BE UNDONE. PLEASE MAKE SURE THAT YOU ARE VERY CAREFUL BEFORE CONFIRMING THIS.')) {
            $.ajax('/api/ipanel/status/', {
                type: 'DELETE',
                data: {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: () => {
                    $('#statusModalTitle').html('Success!');
                    $('#statusModalContent').html('All PNM objects for IPanel have been successfully deleted.');
                    $('#statusModal').modal();
                },
                error: (err) => {
                    $('#statusModalTitle').html('Error');
                    $('#statusModalContent').html('Unexpected error generating PNM statuses with text ' + err.responseText + ' Please contact an admin.');
                    $('#statusModal').modal();
                }
            });
        }
    });

    $('#generateForm').on('submit', function (event) {
        event.preventDefault();

        if (confirm('Please confirm that you have deleted all the old statuses before continuing!')) {
            const data = {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'start': 1,
                'end': $('#number').val()
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