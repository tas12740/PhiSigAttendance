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

                for (let i in response) {
                    const currDiv = $('<div class="pnm"></div>');

                    const pnm = $('<p>PNM ' + i + '</p>');
                    currDiv.append(pnm);

                    const result = $('<p>' + response[i][0] + '</p>');
                    currDiv.append(result);

                    const percent = $('<p>' + response[i][1] + '%</p>');
                    currDiv.append(percent);
                    
                    $('#results').append(currDiv);
                }
            }, error: (err) => {
                $('#resultsModalTitle').html('Error!');
                $('#resultsModalContent').html(err.responseText);
                $('#resultsModal').modal();
            }
        })
    })
});