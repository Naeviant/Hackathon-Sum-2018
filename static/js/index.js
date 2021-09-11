$(document).on("ready", function() {
    $.post("http://127.0.0.1:5000/exists", {}, function(response) {
        setTimeout(function() {
            if (response.body === true) {
                window.location = "home.html";
            }
            else {
                window.location = "preferences.html";
            }
        }, 3000);
    });
});