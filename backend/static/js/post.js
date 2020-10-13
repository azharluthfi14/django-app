$(document).on('submit', '#post-form', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/predict/',
        data: {
            fixed_acidity: $('#fixed_acidity').val(),
            volatile_acidity: $('#volatile_acidity').val(),
            citric_acid: $('#citric_acid').val(),
            residual_sugar: $('#residual_sugar').val(),
            chlorides: $('#chlorides').val(),
            free_sulfur_dioxide: $('#free_sulfur_dioxide').val(),
            total_sulfur_dioxide: $('#total_sulfur_dioxide').val(),
            density: $('#density').val(),
            pH: $('#pH').val(),
            sulphates: $('#sulphates').val(),
            alcohol: $('#alcohol').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'POST'
        },
        success: function (json) {
            document.forms["post-form"].reset();
            document.getElementById("prediction").innerHTML = json['result']
            document.getElementById("fa").innerHTML = json['fixed_acidity']
            document.getElementById("va").innerHTML = json['volatile_acidity']
            document.getElementById("ca").innerHTML = json['citric_acid']
            document.getElementById("rs").innerHTML = json['residual_sugar']
            document.getElementById("c").innerHTML = json['chlorides']
            document.getElementById("fsd").innerHTML = json['free_sulfur_dioxide']
            document.getElementById("tsd").innerHTML = json['total_sulfur_dioxide']
            document.getElementById("d").innerHTML = json['density']
            document.getElementById("ph").innerHTML = json['pH']
            document.getElementById("s").innerHTML = json['sulphates']
            document.getElementById("a").innerHTML = json['alcohol']
        },
        error: function (xhr, errmsg, err) {

        }
    });
});