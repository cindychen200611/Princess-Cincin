const btns = document.querySelectorAll('button');

for (let i=0; i<btns.length; i++) {
    $(btns[i]).click(function(event) {
        var form = $('#itinerary');
        var id = `btn${i+1}`;
        var url = form.prop('action');
        var type = form.prop('method');
        var formData = {'itinerary': document.getElementById(id).value};

        console.log(`form: ${form}\nurl: ${url}\ntype: ${type}`);
        for (var key in formData) { console.log('formData', key, formData[key]);}

        send_form(form, url, type, modular_ajax, formData);
    })
}

function send_form(form, url, type, inner_ajax, formData) {
    event.preventDefault();
    inner_ajax(url, type, formData);
}

function modular_ajax(url, type, formData) {
    // Most simple modular AJAX building block
    $.ajax({
        url: url,
        type: type,
        data: formData,
    });
};

for (let i=0; i<btns.length; i++) {
    btns[i].addEventListener('click', function(e) {
        if (btns[i].className == 'clicked') {
            btns[i].className = '';
            btns[i].textContent = 'Add to Itinerary';
        }
        else {
            btns[i].className = 'clicked';
            btns[i].textContent = 'Remove From Itinerary';
        }
    })
}