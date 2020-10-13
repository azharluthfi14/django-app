Pace.on("done", function () {
    console.log("finished");
    $('body').fadeIn(4500).delay(1000);
});

$(document).on('click', '#process', function (e) {
    Pace.restart();
});

paceOptions = {
    ajax: false, // disabled
    document: true, // enabled
    eventLag: false, // disabled
    elements: {
        selectors: ['#post-form']
    }
};

