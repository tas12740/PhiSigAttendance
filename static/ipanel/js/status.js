$(document).ready(function () {
    $.ajax('/api/ipanelStatus/', {
        type: 'GET',
        success: (response) => {
            console.log(response);
        },
        error: (err) => {
            console.log(err);
        }
    })
})