$(document).ready(function () {
    $('#cutOffsForm').on('submit', function (event) {
        event.preventDefault();

        const data = {
            'cutoff': $('#cutoff').val(),
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
        }

        $.ajax('/api/ipanelResults/', {
            type: 'POST',
            data: data,
            success: (response) => {
                $('#results').empty();
                $('#results').append('<ul id="resultsList"></ul>');
                for(let i in response) {
                    $('#resultsList').append('<li>PNM ' + i + ': ' + response[i] + '</li>');
                }
            }, error: () => {
                $('#resultsModalTitle').html('Error!');
                $('#resultsModalContent').html('Unexpected error. Please see an admin.');
                $('#resultsModal').modal();
            }
        })
    })
});