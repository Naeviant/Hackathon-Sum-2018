$("#submit").on("click", function() {
    // Create Request Wrapper
    var payload = {};

    // Create Validation Variable
    var valid = true;

    // Question 1
    if ($("#q1 #yes").is(":checked") === true) {
        payload["q1"] = true;
    }
    else if ($("#q1 #no").is(":checked") === true) {
        payload["q1"] = false;
    }
    else {
        valid = false;
        $("#q1").addClass("invalid-wrapper");
    }

    // Question 2
    if ($("#q2 #yes").is(":checked") === true) {
        payload["q2"] = true;
    }
    else if ($("#q2 #no").is(":checked") === true) {
        payload["q2"] = false;
    }
    else {
        valid = false;
        $("#q2").addClass("invalid-wrapper");
    }

    // Question 3
    if ($("#q3 #yes").is(":checked") === true) {
        payload["q3"] = true;
    }
    else if ($("#q3 #no").is(":checked") === true) {
        payload["q3"] = false;
    }
    else {
        valid = false;
        $("#q3").addClass("invalid-wrapper");
    }

    if (valid === true) {
        $.post("http://127.0.0.1:5000/submit", JSON.stringify(payload), function() {
            setTimeout(function() {
              window.location = "home.html";
            }, 3000);
            M.toast({
                html: "Submission complete. Returning to home page...",
                displayLength: 3000,
                classes: "rounded"
            });
        });
    }
    else {
        // Handle Invalid Results
        setTimeout(function() {
          $("#q1").removeClass("invalid-wrapper");
          $("#q2").removeClass("invalid-wrapper");
          $("#q3").removeClass("invalid-wrapper");
        }, 3000);
        M.toast({
            html: "Please complete all questions to continue.",
            displayLength: 4000,
            classes: "rounded"
        });
    }
    
});