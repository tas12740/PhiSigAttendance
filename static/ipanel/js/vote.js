const gen_vote = function (num) {
    const pnmDiv = $('<div class="pnm" id="pnm' + num + '"></div>');

    const radioYesDiv = $('<div class="form-check"></div>');
    const inputYes = $('<input required class="form-check-input" type="radio" name="vote' + num + '" id="voteYes' + num + '" value="Y">');
    const labelYes = $('<label class="form-check-label" for="voteYes' + num + '">Yes</label>');
    radioYesDiv.append(inputYes);
    radioYesDiv.append(labelYes);

    const radioNoDiv = $('<div class="form-check"></div>');
    const inputNo = $('<input required class="form-check-input" type="radio" name="vote' + num + '" id="voteNo' + num + '" value="N">');
    const labelNo = $('<label class="form-check-label" for="voteNo' + num + '">No</label>');
    radioNoDiv.append(inputNo);
    radioNoDiv.append(labelNo);

    const radioAbstainDiv = $('<div class="form-check"></div>');
    const inputAbstain = $('<input required class="form-check-input" type="radio" name="vote' + num + '" id="voteAbstain' + num + '" value="A">');
    const labelAbstain = $('<label class="form-check-label" for="voteAbstain' + num + '">Abstain</label>');
    radioAbstainDiv.append(inputAbstain);
    radioAbstainDiv.append(labelAbstain);

    const header = $('<h3 class="my-2">PNM ' + num + '</h3>');

    pnmDiv.append(header);
    pnmDiv.append(radioYesDiv);
    pnmDiv.append(radioNoDiv);
    pnmDiv.append(radioAbstainDiv);

    return pnmDiv;
}

$(document).ready(function () {
    $.ajax('/api/ipanelOpens/', {
        type: 'GET',
        success: (response) => {
            const pnms = response.pnms;
            pnms.sort();

            if (pnms.length == 0) {
                $('#voteForm').remove();
                const message = $('<p>There are no PNMs which are unlocked to vote on right now. Please stay tuned!');
                $('#votes').append(message);
            } else {
                $('.pnm').remove();

                for (const pnm of pnms) {
                    const res = gen_vote(pnm);
                    res.insertBefore('#votebtn');
                    res.hide();
                }

                $('.pnm').slideDown(1000);
            }
        },
        error: () => {
            $('#voteForm').remove();
            const errMessage = $('<p>There was a problem fetching PNMs which can currently be voted upon. Please stay tuned!');

            $('#votes').append(errMessage);
        }
    });

    $('#voteForm').on('submit', function (event) {
        event.preventDefault();

        let data = {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'onyen': $('#onyen').val(),
            'code': $('#code').val()
        }

        const pnmDivs = $('.pnm');

        for (const pnmDiv of pnmDivs) {
            const num = $(pnmDiv).attr('id').slice(3);
            data['' + num] = $('input[name="vote' + num + '"]:checked').val();
        }

        $.ajax('/api/ipanelVote/', {
            type: 'POST',
            data: data,
            success: (response) => {
                $('#voteModalTitle').html('Success!');

                let success_pnms = response.success_pnms;
                success_pnms = success_pnms.map((val) => 'PNM #' + val);
                const successText = (success_pnms.length == 0) ? 'No votes were successfully recorded. ' : 'The following votes were successfully recorded: ' + success_pnms.join(', ') + '. ';

                let errorText;
                if (response.error_pnms.length == 0) {
                    errorText = '';
                    $('#voteErrorContent').hide();
                } else {
                    let error_pnms = response.error_pnms;
                    error_pnms = error_pnms.map((val) => 'PNM #' + val);

                    const error_num = error_pnms.length;
                    errorText = 'The following failed: ';
                    for (let i = 0; i < error_num; i++) {
                        errorText += error_pnms[i] + ' (' + response.error_statuses[i] + ')';
                        if (i != error_num - 1) {
                            errorText += ', ';
                        }
                    }
                    errorText += '.';
                    $('#voteErrorContent').show();
                    $('#voteErrorContent').html(errorText);
                }
                $('#voteModalContent').html(successText);
                $('#voteModal').modal();

                $('#votes').slideUp(2000);
            },
            error: (err) => {
                $('#voteModalTitle').html('Error!');
                $('#voteModalContent').html(err.responseText);
                $('#voteModal').modal();
            }
        });
    })
});