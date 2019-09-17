$(document).ready(function () {
    $.ajax('/api/findEvent/', {
        type: 'GET',
        data: {
            'recruitment': true
        },
        success: (response) => {
            $('#header').html(response.eventName);
            $('#eventType').val(response.eventType);
            $('#eventName').val(response.eventName);
            $('#onyenFormDiv').slideDown(2000);
            console.log(response);
        },
        error: (err) => {
            $('#header').html(err.responseText);
        }
    });

    $('#onyenForm').on('submit', function (event) {
        event.preventDefault();

        const data = {
            'onyen': $('#onyen').val(),
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'event_type': $('#eventType').val(),
            'event_name': $('#eventName').val()
        }

        $.ajax('/api/recruitmentOnyen/', {
            type: 'POST',
            data: data,
            success: (response) => {
                $('#checkinModalTitle').html('Success!');
                $('#checkinModalContent').html('Welcome back to Phi Sig, ' + response.name + '!');
                $('#checkinModal').modal();
                $('#onyen').val('');
            },
            error: () => {
                $('#additionalInformationDiv').slideDown(2000);
                $('#onyenAdd').val($('#onyen').val());
                $('#onyenFormDiv').slideUp(2000);
            }
        });
    });

    $('#additionalInformationForm').on('submit', function (event) {
        event.preventDefault();
        const data = {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'onyen': $('#onyenAdd').val(),
            'first_name': $('#firstName').val(),
            'last_name': $('#lastName').val(),
            'email': $('#email').val(),
            'event_type': $('#eventType').val(),
            'event_name': $('#eventName').val()
        }

        console.log(data);

        $.ajax('/api/pnmCheckIn/', {
            type: 'POST',
            data: data,
            success: () => {
                $('#checkinModalTitle').html('Success!');
                $('#checkinModalContent').html('Welcome to Phi Sig!');
                $('#checkinModal').modal();
                $('#onyen').val('');
                $('#onyenAdd').val('');
                $('#firstName').val('');
                $('#lastName').val('');
                $('#email').val('');
                $('#additionalInformationDiv').slideUp(2000);
                $('#onyenFormDiv').slideDown(2000);
            },
            err: (err) => {
                console.log(err);
            }
        });
    })

    $('#onyenFormDiv').hide();
    $('#additionalInformationDiv').hide();
});