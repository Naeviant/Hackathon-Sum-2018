$(document).on("ready", function() {
    $.post("http://127.0.0.1:5000/populate", {}, function(response) {
        if (response.status === 200) {
            // Question 1
            if (response.body["q1"] === true) {
                $("#q1 #yes").prop("checked", true);
                $("#q1 #no").prop("checked", false)
            }
            else if (response.body["q1"] === false) {
                $("#q1 #no").prop("checked", true);
                $("#q1 #yes").prop("checked", false)
            }

            // Question 2
            if (response.body["q2"] === true) {
                $("#q2 #yes").prop("checked", true);
                $("#q2 #no").prop("checked", false)
            }
            else if (response.body["q2"] === false) {
                $("#q2 #no").prop("checked", true);
                $("#q2 #yes").prop("checked", false)
            }

            // Question 3
            if (response.body["q3"] === true) {
                $("#q3 #yes").prop("checked", true);
                $("#q3 #no").prop("checked", false)
            }
            else if (response.body["q3"] === false) {
                $("#q3 #no").prop("checked", true);
                $("#q3 #yes").prop("checked", false)
            }
        }
    });
});