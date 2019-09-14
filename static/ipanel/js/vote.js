const gen_vote = function (num) {
    const radioYesDiv = $('<div class="form-check pnm"></div>');
    const inputYes = $('<input required class="form-check-input" type="radio" name="vote' + num + '" id="voteYes' + num + '" value="Y">');
    const labelYes = $('<label class="form-check-label" for="voteYes' + num + '">Yes</label>');
    radioYesDiv.append(inputYes);
    radioYesDiv.append(labelYes);

    const radioNoDiv = $('<div class="form-check pnm"></div>');
    const inputNo = $('<input required class="form-check-input" type="radio" name="vote' + num + '" id="voteNo' + num + '" value="N">');
    const labelNo = $('<label class="form-check-label" for="voteNo' + num + '">No</label>');
    radioNoDiv.append(inputNo);
    radioNoDiv.append(labelNo);

    const radioAbstainDiv = $('<div class="form-check pnm"></div>');
    const inputAbstain = $('<input required class="form-check-input" type="radio" name="vote' + num + '" id="voteAbstain' + num + '" value="A">');
    const labelAbstain = $('<label class="form-check-label" for="voteAbstain' + num + '">Abstain</label>');
    radioAbstainDiv.append(inputAbstain);
    radioAbstainDiv.append(labelAbstain);

    const header = $('<h3 class="pnm my-2">PNM ' + num + '</h3>');

    const arr = [header, radioYesDiv, radioNoDiv, radioAbstainDiv];
    return arr;
}

$(document).ready(function () {
    $('#voteGenForm').on('submit', function (event) {
        event.preventDefault();

        const start = $('#start').val();
        const end = $('#end').val();
        if (end <= start) {
            alert('End cannot be less than or equal to start.');
            return;
        }

        $('.pnm').remove();
        $('#voteGen').slideUp(2000);

        for (let i = start; i <= end; i++) {
            const res = gen_vote(i);
            for (let k = 0; k < res.length; k++) {
                res[k].insertBefore('#votebtn');
            }
        }

        $('#votes').slideDown(2000);
    });

    $('#votes').hide();

    $('#voteForm').on('submit', function (event) {
        event.preventDefault();

        const start = $('#start').val();
        const end = $('#end').val();

        let data = {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'onyen': $('#onyen').val(),
            'code': $('#code').val()
        }
        for (let i = start; i <= end; i++) {
            data['' + i] = $('input[name="vote' + i + '"]:checked').val();
        }

        $.ajax('/api/ipanelVote/', {
            type: 'POST',
            data: data,
            success: () => {
                $('#voteModalTitle').html('Success!');
                $('#voteModalContent').html('Your votes have been successfully recorded.');
                $('#voteModal').modal();

                $('#votes').slideUp(2000);
                $('#start').val('');
                $('#end').val('');
                $('#voteGen').slideDown(2000);
            },
            error: (err) => {
                $('#voteModalTitle').html('Error!');
                $('#voteModalContent').html(err.responseText);
                $('#voteModal').modal();
            }
        });
    })
});