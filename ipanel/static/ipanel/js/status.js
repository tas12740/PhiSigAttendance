const add_row = (tbody, key, status) => {
    const row = $('<tr></tr>');
    const header = $('<th scope="row">' + key + '</th>');
    const first_cell = $('<td></td>');
    const second_cell = $('<td></td>');

    const first_check = $('<input type="checkbox" id="pnm-' + key + '-lock" value="L"' + ((status == 'L') ? 'checked' : '') + '>');
    first_cell.append(first_check);

    const second_check = $('<input type="checkbox" id="pnm-' + key + '-open" value="O"' + ((status != 'L') ? 'checked' : '') + '>');
    second_cell.append(second_check);

    first_check.on('click', function () {
        second_check.prop('checked', !second_check.prop('checked'));
    });
    second_check.on('click', function () {
        first_check.prop('checked', !first_check.prop('checked'));
    });

    row.append(header);
    row.append(first_cell);
    row.append(second_cell);
    tbody.append(row);
}

const get_number = (id) => {
    const split = id.split('-');
    return split[1];
}

$(document).ready(function () {
    $.ajax('/api/ipanelStatus/', {
        type: 'GET',
        success: (response) => {
            const tbody = $('#tbodyStatus');
            for (let key in response) {
                if (response.hasOwnProperty(key)) {
                    add_row(tbody, key, response[key]);
                }
            }
        },
        error: (err) => {
            $('#statusModalTitle').html('Error');
            $('#statusModalContent').html('Unexpected error loading PNM statuses with text ' + err.responseText + '. Please contact an admin.');
            $('#statusModal').modal();
        }
    });

    $('#statusForm').on('submit', function (event) {
        event.preventDefault();
        const rows = $('tbody tr');
        const num_rows = rows.length;

        let data = {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
        };

        for (let i = 0; i < num_rows; i++) {
            const curr_row = rows.eq(i);
            const checked_box = curr_row.find(':checked');
            const val = checked_box.val();
            const number = get_number(checked_box.attr('id'));
            data[number] = val;
        }

        $.ajax('/api/ipanelStatus/', {
            type: 'POST',
            data: data,
            success: (response) => {
                $('#statusModalTitle').html('Success!');
                if (response.error_pnms.length == 0 && response.success_pnms.length == 0) {
                    $('#statusModalContent').html('The PNMs\' statuses were successfully updated to reflect the state of the table.');
                } else {
                    const success_pnms = response.success_pnms.map((val) => 'PNM #' + val);
                    const error_pnms = response.error_pnms.map((val) => 'PNM #' + val);
                    const failedText = (error_pnms.length == 0) ? '' : 'The following PNMs\' statuses failed to change: ' + error_pnms.join(', ') + '.';
                    if (failedText == '') {
                        $('#statusModalErrors').hide();
                    } else {
                        $('#statusModalErrors').html(failedText);
                    }
                    $('#statusModalContent').html('The following PNMs\' statuses successfully changed: ' + success_pnms.join(', ') + '.');
                }
                $('#statusModal').modal();
            },
            error: (err) => {
                $('#statusModalTitle').html('Error');
                $('#statusModalContent').html('Unexpected error changing PNM statuses with text ' + err.responseText + '. Please contact an admin.');
                $('#statusModal').modal();
            }
        });
    })
})