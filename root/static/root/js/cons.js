$(document).ready(function () {
    $('#onyen-form').on('submit', function (e) {
        e.preventDefault();

        const onyen = $('#onyen').val().toLowerCase();
        const numbers = /^[0-9]+$/;
        if (onyen.match(numbers)) {
            alert("Please submit your onyen, not your PID!");
            return;
        }

        const data = {
            'onyen': onyen,
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
        }

        $.ajax('/api/cons/', {
            type: 'POST',
            data: data,
            success: (response) => {
                $('#onyen-form').slideUp(2000);
                console.log(response);
                for (const key in response) {
                    const div = $('<div class="position"></div>');
                    const header = $('<h2>' + key + '</h2>');
                    div.append(header);

                    for (const person in response[key]) {
                        const personHeader = $('<h3>' + person + '</h3>');
                        div.append(personHeader);

                        const list = $('<ul></ul>');
                        for (const con of response[key][person]) {
                            const listItem = $('<li>' + con + '</li>');
                            list.append(listItem);
                        }
                        div.append(list);
                    }

                    $('#cons-div').append(div);
                }
            },
            error: (err) => {
                console.log(err);
            }
        });
    })
})